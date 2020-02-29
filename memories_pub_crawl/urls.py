"""memories_pub_crawl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from booking.views import ThankYouPageView,payment_canceled
from booking import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('', include('user.urls')),
    path('blog/', include('blog.urls')),
    path('book-now/', include('booking.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('thank-you/', ThankYouPageView.as_view(), name='thank-you'),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('process-payment/', views.process_payment, name='process_payment'),
    path('payment-done/', views.payment_done, name='payment_done'),
    path('payment-cancelled/', payment_canceled.as_view(), name='payment-cancelled'),
    path('payment-url/', views.buy_my_item),
    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
