from django.urls import path
from . import views

app_name = "contact_app" 

urlpatterns = [
    path('', views.contact, name='contact'),
    path('pdf/', views.create_pdf, name='contact_pdf')
]