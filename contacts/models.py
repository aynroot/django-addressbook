from __future__ import unicode_literals

from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=64)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return ' '.join((self.first_name, self.last_name))
