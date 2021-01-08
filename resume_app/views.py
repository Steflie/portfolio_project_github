from django.shortcuts import render
from .models import Jobs, Education, Publications, Languages, Volunteer

# Create your views here.

def resume(request):
    jobs = Jobs.objects
    educations = Education.objects
    publications = Publications.objects
    languages = Languages.objects
    volunteers = Volunteer.objects
    return render(request, 'resume_app/resume.html', {
        'jobs':jobs, 
        'educations':educations,
        'publications':publications,
        'languages':languages,
        'volunteers':volunteers,
        })