from django.urls import path
from .views import HomePageView, PackagePageView, GalleryPageView, TermsAndConditionsPageView, PrivacyPolicyPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('packages/', PackagePageView.as_view(), name='packages'),
    path('gallery/', GalleryPageView.as_view(), name='gallery'),
    path('terms-and-conditions/', TermsAndConditionsPageView.as_view(), name='terms-and-conditions'),
    path('privacy-policy/', PrivacyPolicyPageView.as_view(), name='privacy-policy'),

]
