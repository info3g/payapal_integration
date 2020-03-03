from django.views.generic import View
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Packages, Gallery

class HomePageView(View):
    def get(self, *args, **kwargs):
        try:
            packages = Packages.objects.all()

            context = {
                'packages': packages,
            }

            return render(self.request, 'pages/index.html', context)
        except ObjectDoesNotExist:
            return redirect('/')


class PackagePageView(View):
    def get(self, *args, **kwargs):
        try:
            packages = Packages.objects.all()

            context = {
                'packages': packages,
            }

            return render(self.request, 'pages/packages.html', context)
        except ObjectDoesNotExist:
            return redirect('/')


class GalleryPageView(View):
    def get(self, *args, **kwargs):
        gallery = Gallery.objects.all()

        context = {
            'gallery': gallery,
        }

        return render(self.request, 'pages/gallery.html', context)


class TermsAndConditionsPageView(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'pages/terms_and_conditions.html')

class PrivacyPolicyPageView(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'pages/privacy_policy.html')
