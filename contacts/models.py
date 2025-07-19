import re
from django.core.exceptions import ValidationError
from django.db import models

class ContactDetails(models.Model):
    ID = models.BigAutoField(primary_key=True)
    FirstName = models.CharField(max_length=200)
    LastName = models.CharField(max_length=200)
    Address = models.CharField(max_length=200)
    Email = models.EmailField(max_length=200, unique=True)
    PhoneNumber = models.CharField(max_length=10, unique=True)

    class Meta:
        unique_together = ('FirstName','LastName')
        
    def clean(self):
        super().clean()

        email_regex = r"[^@]+@[^@]+\.[^@]+"
        if not re.match(email_regex, self.Email):
            raise ValidationError({'Email': 'Not a valid email address.'})

        if not self.PhoneNumber.isdigit():
            raise ValidationError({'PhoneNumber': 'Phone number must contain only digits.'})

        if len(self.PhoneNumber) != 10:
            raise ValidationError({'PhoneNumber': 'Phone number must be exactly 10 digits.'})
