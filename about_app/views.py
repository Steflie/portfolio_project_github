from django.shortcuts import render
from .models import About

# Create your views here.
def about(request):
    text = About.objects.first()
    return render(request,'about_app/about.html', {'text':text})