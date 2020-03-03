"""paypalintegrationproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from payment import views as api_views
from django.views.generic import TemplateView
urlpatterns = [
    url(r'^testcode/$',api_views.testcode),
    url(r'^testfunction/$',api_views.testfucntion),
    url(r'^admin/', admin.site.urls),

    url(r'^paypal/', include('paypal.standard.ipn.urls')),
    url(r'^payment_process/$', api_views.payment_process,
        name='payment_process'),
    url(r'^payment_done/$',TemplateView.as_view(
            template_name="payment_done.html"),
        name='payment_done'),
    url(r'^payment_canceled/$',TemplateView.as_view(
            template_name="payment_canceled.html"),
        name='payment_canceled'),
    url(r'^payment-url/$', api_views.buy_my_item),

]
