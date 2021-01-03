from django.shortcuts import render
from .models import ContactDetails
from django.core.mail import send_mail

# Create your views here.


def contact(request):
    """Render the contact html page"""
    contacts = ContactDetails.objects
    return render(request, 'contact_app/contact.html', {"contacts":contacts})