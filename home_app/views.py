from django.shortcuts import render

# Create your views here.


def home(request):
    """Home Page"""
    return render(request, 'home_app/home.html')