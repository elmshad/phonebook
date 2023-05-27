from django import forms
from .models import *

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

class NumberForm(forms.ModelForm):
    class Meta:
        model = Number
        fields = "__all__"



NumberFormSet = forms.inlineformset_factory(
    Contact, Number, form=NumberForm, extra=10)
