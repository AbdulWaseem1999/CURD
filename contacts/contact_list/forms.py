from django import forms
from .models import contact


class ContactForm(forms.ModelForm):
    class Meta:
        model=contact
        fields=['name','email','mobile']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','id':'name'}),
            'email':forms.EmailInput(attrs={'class':'form-control','id':'email'}),
            'mobile':forms.TextInput(attrs={'class':'form-control','id':'mobile'}),
        }
