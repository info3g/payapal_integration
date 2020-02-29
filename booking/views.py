from django.urls import reverse
from pages.models import Packages
from django.contrib import messages
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views.generic import View, FormView
from django.core.exceptions import ObjectDoesNotExist
from .extras import transact, generate_client_token

from .models import Booking, Customer, Coupon, Transaction
from .forms import BookNowForm
import json


class CheckoutPageView(View):
    def get(self, *args, **kwargs):

        package = self.kwargs['package']
        self.request.session['choosen_package'] = package
        choosen_package = get_object_or_404(Packages, slug=package)

        dict = {}

        for coupon in Coupon.objects.all():
            dict[coupon.coupon_name] = coupon.coupon_discount

        r = json.dumps(dict)
        serialized_coupon = r

        serialized_package = serializers.serialize('json', [ choosen_package, ])

        context = {
            'choosen_package': choosen_package,
            'serialized_coupon': serialized_coupon,
            'serialized_package': serialized_package,
            'discount_price': choosen_package.discount_price,
            'price': choosen_package.price,
        }

        return render(self.request, 'booking/checkout.html', context)

    def post(self, *args, **kwargs):
        form = BookNowForm(self.request.POST or None)
        package = self.kwargs['package']
        self.request.session['choosen_package'] = package
        choosen_package = get_object_or_404(Packages, slug=package)

        try:
            print(form.is_valid())
            if form.is_valid():
                print(form.errors)
                tour_date = form.cleaned_data.get('tour_date')
                headCount = form.cleaned_data.get('headCount')
                buyer_name = form.cleaned_data.get('buyer_name')
                buyer_email = form.cleaned_data.get('buyer_email')
                buyer_country = form.cleaned_data.get('buyer_country')
                buyer_zip = form.cleaned_data.get('buyer_zip')
                buyer_address = form.cleaned_data.get('buyer_address')
                payment_type = form.cleaned_data.get('payment_type')
                docs = form.cleaned_data.get('docs')
                totalPrice = form.cleaned_data.get('totalPrice')
                couponName = form.cleaned_data.get('couponName')

                address = str(buyer_zip) + ', ' + buyer_address

                try:
                    find_customer = Customer.objects.get(email=buyer_email)
                    existing_customer_id = find_customer.id
                    cust = get_object_or_404(Customer, id=existing_customer_id)

                    self.request.session['customer_id'] = existing_customer_id
                except Exception:
                    customer = Customer(
                        name = buyer_name,
                        email = buyer_email,
                        address = buyer_address,
                        headcount = headCount,
                        payment_type = 'online',

                    )
                    customer.save()

                    cust = get_object_or_404(Customer, id=customer.id)

                    self.request.session['customer_id'] = cust.id

                try:
                    find_coupon = Coupon.objects.get(coupon_name=couponName)
                    print(find_coupon)
                    print('coupon gets here')
                    coupon_price = find_coupon.coupon_discount
                    print(coupon_price)
                except Exception:
                    coupon_price = 0
                    print('does it get here?')

                if choosen_package.discount_price:
                    calc_price = headCount * (choosen_package.discount_price - coupon_price)
                else:
                    calc_price = headcount * (choosen_package.price - coupon_price)

                booking = Booking(
                    customer_name = buyer_name,
                    customer_email = buyer_email,
                    headcount = headCount,
                    customer_id = cust.id,
                    date_string = tour_date,
                    date = tour_date,
                    price = calc_price,
                    package = choosen_package,
                    type_of_booking = 'online',
                    coupon_name = couponName,
                    terms_and_conditions_accepted = True,
                )
                booking.save()

                self.request.session['booking_id'] = booking.id

                return redirect(reverse('payment', kwargs={'package': choosen_package.slug}))

        except ObjectDoesNotExist:
            return redirect(reverse('checkout', kwargs={'package': choosen_package.slug}))

class PaymentPageView(View):
    def get(self, *args, **kwargs):
        customer_id = self.request.session['customer_id']
        booking_id = self.request.session['booking_id']

        customer = get_object_or_404(Customer, id=customer_id)
        booking = get_object_or_404(Booking, id=booking_id)

        package = self.kwargs['package']
        choosen_package = get_object_or_404(Packages, slug=package)

        client_token = generate_client_token()

        context = {
            'customer': customer,
            'booking': booking,
            'client_token': client_token,
            'choosen_package': choosen_package,
        }
        return render(self.request, 'booking/payment.html', context)
    def post(self, *args, **kwargs):
        customer_id = self.request.session['customer_id']
        booking_id = self.request.session['booking_id']

        customer = get_object_or_404(Customer, id=customer_id)
        booking = get_object_or_404(Booking, id=booking_id)

        package = self.request.session['choosen_package']
        choosen_package = get_object_or_404(Packages, slug=package)

        amount = int(booking.price)

        result = transact({
            'amount': amount,
            'payment_method_nonce': self.request.POST['payment_method_nonce'],
            'options': {
                "submit_for_settlement": True
            }
        })

        if result.is_success or result.transaction:

            print(result)
            print(result.transaction.id)
            booking.payment_made = True
            booking.save()
            transaction = Transaction(
                bt_transaction_id = result.transaction.id,
                customer_id = customer.id,
                booking_id = booking.id,
                response = result
            )
            transaction.save()

            return redirect('thank-you')
        else:
            for x in result.errors.deep_errors:
                print(x)
                booking.payment_made = False
                transaction = Transaction(
                    bt_transaction_id = result.transaction.id,
                    customer_id = customer.id,
                    booking_id = booking.id,
                    response = x
                )
                messages.info(self.request, x)
            return redirect(reverse('payment', kwargs={'package': choosen_package.slug}))

class ThankYouPageView(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'booking/thank_you.html')

from django.contrib import messages
from django.conf import settings
from decimal import Decimal
from paypal.standard.forms import PayPalPaymentsForm
# from .models import Product, Order, LineItem
# from .forms import CartForm, CheckoutForm

def process_payment(request):
    customer_id = request.session['customer_id']
    booking_id = request.session['booking_id']

    customer = get_object_or_404(Customer, id=customer_id)
    booking = get_object_or_404(Booking, id=booking_id)
    host = request.get_host()
    amount = int(booking.price)
    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': amount,
        'item_name':"tour" ,
        'invoice': booking_id,#need to write new invoice evry time
        'currency_code': 'USD',
        'notify_url': 'http://{}{}'.
            format(host, reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.
            format(host, reverse('thank-you')),
        'cancel_return': 'http://{}{}'.format(host, reverse('payment-cancelled')),
        
    
    }
    print(paypal_dict)

    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'booking/paypal.html',
                {'form': form})



from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt
# from .models import Product, Order, LineItem
#...
 
 

@csrf_exempt
def payment_done(request):
    return render(request, 'booking/payment_done.html')
 
class payment_canceled(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'booking/payment_cancelled.html')



from paypal.pro.views import PayPalPro

def nvp_handler(nvp):
    # This is passed a PayPalNVP object when payment succeeds.
    # This should do something useful!
    return render(request, 'booking/payment_done.html')

def buy_my_item(request):
    customer_id = request.session['customer_id']
    booking_id = request.session['booking_id']

    customer = get_object_or_404(Customer, id=customer_id)
    booking = get_object_or_404(Booking, id=booking_id)
  
    amount = int(booking.price)
    item = {"amt": amount,  # amount to charge for item
            "inv": "inventory",         # unique tracking variable paypal
            "custom": "tracking",       # custom tracking variable for you
            "cancelurl": "/payment-cancelled/",  # Express checkout cancel url
            "returnurl": "/thank-you/"}  # Express checkout return url
    print("items",item)
    gh=request.session['role_name'] = amount
    ppp = PayPalPro(
              item=item,                            # what you're selling
              payment_template="booking/credit.html",      # template name for payment
              confirm_template="confirmation.html", # template name for confirmation
              success_url="/thank-you/",              # redirect location after success
              nvp_handler=nvp_handler)
    print("ppp",ppp)
    r=request.GET.get("transaction_id")
    print(r)
    print(request)
    print("ppp",type(ppp))
    print("ppp",ppp.confirm_form_cls,"context")
    print("ppp",ppp.__dir__())

    # print(ppp.submit_for_settlement())
    # if ppp :

    #     print(ppp)
    #     print(ppp.transaction.id)
    #     booking.payment_made = True
    #     booking.save()
    #     transaction = Transaction(
    #         bt_transaction_id = ppp.transaction.id,
    #         customer_id = customer.id,
    #         booking_id = booking.id,
    #         response = ppp
    #     )
    #     transaction.save()
    # print(ppp.get)
    # print(ppp.value)

    return ppp(request)