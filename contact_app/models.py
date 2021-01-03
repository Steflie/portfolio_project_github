from django.db import models

# Create your models here.


class ContactDetails(models.Model):
    """The details of the contact"""
    contact_icon = models.ImageField(upload_to='images/')
    contact_name = models.CharField(max_length=50)
    contact_info = models.CharField(max_length=50)
    contact_url = models.URLField(max_length=200, default='#')
    