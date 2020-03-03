from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from payment.models import State
from django.core import serializers
from django.conf import settings
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from paypal.standard.forms import PayPalPaymentsForm
from django.forms.models import model_to_dict
# from orders.models import order
def payment_process(request):

    host = request.get_host()
    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': '10',
        'item_name': 'Item_Name_xyz',
        'invoice': 'daljit123',#need to write new invoice evry time
        'currency_code': 'USD',
        'notify_url': 'http://{}{}'.
            format(host, reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.
            format(host, reverse('payment_done')),
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'payment_process.html',
                {'form': form})

def testcode(request):

    return render(request,"test.html")
import json
def testfucntion(request):
    id = request.GET["myid"]
    all_pro = State.objects.all()
    d = {}
    for i in all_pro:
        d[i.statid] = i.statename

    return JsonResponse(d, safe=False)


from paypal.pro.views import PayPalPro






def nvp_handler(nvp):
    # This is passed a PayPalNVP object when payment succeeds.
    # This should do something useful!
    pass

def buy_my_item(request):
    item = {"paymentrequest_0_amt": "10.00",  # amount to charge for item
            "inv": "inventory",         # unique tracking variable paypal
            "custom": "tracking",       # custom tracking variable for you
            "cancelurl": "http://...",  # Express checkout cancel url
            "returnurl": "http://..."}  # Express checkout return url
    print(item)

    ppp = PayPalPro(
              item=item,                            # what you're selling
              payment_template="payment_process.html",      # template name for payment
              confirm_template="confirmation.html", # template name for confirmation
              success_url="/payment_done/",              # redirect location after success
              nvp_handler=nvp_handler)
    return ppp(request)


    #data=State.objects.all()
    #newdata=dict(data)
    #serialized_obj = serializers.serialize('json', data)

    #serialized = json.dumps(data)



    #for item in all_pro:
    #    item['stateid'] = model_to_dict(item['stateid'])
    #data =serializers.serialize('json', all_pro,fields=["statename"])
    #ty=type(data)
    #nd=json.dumps(data)
    #td=JsonResponse(data,safe=False)
    #dcdata=dict(nd)
    #d={"id":1,"name":"daljit"}

    #return HttpResponse(data)#data#JsonResponse(data)#serialized#_obj#JsonResponse(serialized)


