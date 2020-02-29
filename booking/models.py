from django.db import models
from user.models import User
from pages.models import Packages

PAYMENT_TYPE = (
    ('online', 'online'),
    ('offline', 'offline')
)

TYPE_OF_BOOKING = (
    ('online', 'online'),
    ('offline', 'offline'),
)

class Booking(models.Model):
    customer_name = models.CharField(max_length=60)
    customer_email = models.EmailField()
    headcount = models.FloatField(default=1)
    customer_id = models.FloatField()
    price = models.FloatField(default=None,
                              blank=True,
                              null=True
                              )
    package = models.ForeignKey(Packages,
                                on_delete=models.CASCADE,
                                blank=True,
                                null=True,
                                )
    date_string = models.CharField(max_length=30, default=None, blank=True, null=True)
    date = models.DateField()
    type_of_booking = models.CharField(max_length=20,
                                      choices=TYPE_OF_BOOKING
                                      )
    sold_by = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                blank=True,
                                null=True,
                                )
    payment_made = models.BooleanField(default=False)
    terms_and_conditions_accepted = models.BooleanField(default=False)
    coupon_name = models.CharField(max_length=60,
                                   default=None,
                                   blank=True,
                                   null=True
                                   )


    def __str__(self):
        return f'{self.customer_name} booking on {self.date} with a headcount of {self.headcount}'


class Customer(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    headcount = models.FloatField()

    address = models.CharField(max_length=120, default=None, blank=True, null=True)
    sold_by = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               blank=True,
                               null=True,
                               )
    payment_type = models.CharField(max_length=20,
                                    choices=PAYMENT_TYPE
                                    )

    coupon_id = models.FloatField(default=None,
                                  blank=True,
                                  null=True
                                 )
    invoice_sent = models.BooleanField(default=False)


    def __str__(self):
        return self.name


class Transaction(models.Model):
    bt_transaction_id = models.CharField(max_length=60)
    customer_id = models.IntegerField()
    booking_id = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    response = models.TextField()

    def __str__(self):
        return f'{self.customer_id} azonosítójú vásárló tranzakciója {self.bt_transaction_id}'

class Coupon(models.Model):
    coupon_name = models.CharField(max_length=50)
    coupon_discount = models.FloatField()
    user = models.ForeignKey(User,
                            on_delete=models.CASCADE,
                            blank=True,
                            null=True
                            )

    def __str__(self):
        return self.coupon_name
