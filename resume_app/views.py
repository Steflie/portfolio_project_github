from django.shortcuts import render
from .models import Jobs, Education, Publications

# Create your views here.

def resume(request):
    jobs = Jobs.objects
    educations = Education.objects
    publications = Publications.objects
    return render(request, 'resume_app/resume.html', {
        'jobs':jobs, 
        'educations':educations,
        'publications':publications,
        })