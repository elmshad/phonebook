from django import forms
from .models import Contact, Number


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class NumberForm(forms.ModelForm):
    class Meta:
        model = Number
        fields = ['number']
        widgets = {
            'number': forms.TextInput(attrs={'class': 'form-control'}),
        }


NumberFormSet = forms.modelformset_factory(Number, form=NumberForm, extra=1)
