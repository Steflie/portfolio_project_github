from django.shortcuts import render
from .models import ContactDetails

# Create your views here.


def contact(request):
    """Render the contact html page"""
    contacts = ContactDetails.objects
    return render(request, 'contact_app/contact.html', {"contacts":contacts})