from django.urls import path
from .views import CheckoutPageView, PaymentPageView

urlpatterns = [
    path('<package>/', CheckoutPageView.as_view(), name='checkout'),
    path('<package>/payment/', PaymentPageView.as_view(), name='payment'),

]
