from django.db import models
from django.core.exceptions import ValidationError

class ContactDetails(models.Model):
    ID = models.BigAutoField(primary_key=True)
    FirstName = models.CharField(max_length=200)
    LastName = models.CharField(max_length=200)
    Address = models.CharField(max_length=200)
    Email = models.EmailField(max_length=200, unique=True)
    PhoneNumber = models.CharField(max_length=10)

    def clean(self):
        super().clean()
        if not self.Email.endswith('@gmail.com') and not self.Email.endswith('@outlook.com'):
            raise ValidationError({'Email': 'Only Gmail or Outlook emails are allowed.'})
