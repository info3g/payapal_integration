from django.contrib import admin
from .models import Booking, Customer, Coupon, Transaction


admin.site.register(Booking)
admin.site.register(Customer)
admin.site.register(Coupon)
admin.site.register(Transaction)
