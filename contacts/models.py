from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator


class Contact(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+4917671481627'. "
                                         "Max. 15 digits.")
    phone = models.CharField(validators=[phone_regex], max_length=16)
    email = models.EmailField(blank=True, null=True)
    picture = models.ImageField(upload_to='pictures/', blank=True, null=True)

    def __str__(self):
        return ' '.join((self.first_name, self.last_name))
