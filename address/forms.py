from django import forms
from .models import *

class AddressForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = ('email', 'house_number', 'residential_area', 'street', 'country', 'region', 'city')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['country'].queryset = Country.objects.none()
