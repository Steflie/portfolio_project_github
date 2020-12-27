from django.shortcuts import render

# Create your views here.


def contact(request):
    """Render the contact html page"""
    return render(request, 'contact_app/contact.html')