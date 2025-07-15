from django import forms
from .models import ContactDetails
from django.core.exceptions import ValidationError

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactDetails
        fields = '__all__'

    def clean_Email(self):
        email = self.cleaned_data.get('Email')
        if not email or '@' not in email:
            raise ValidationError("Email is invalid")
        return email
