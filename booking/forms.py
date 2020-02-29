from django import forms


class BookNowForm(forms.Form):
    tour_date = forms.CharField()
    headCount = forms.FloatField()
    buyer_name = forms.CharField()
    buyer_email = forms.EmailField()
    buyer_country = forms.CharField()
    buyer_zip = forms.IntegerField()
    buyer_address = forms.CharField()
    payment_type = forms.CharField()
    docs = forms.BooleanField()
    totalPrice = forms.FloatField()
    couponName = forms.CharField(required=False)
