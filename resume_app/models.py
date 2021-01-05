from django.db import models

# Create your models here.

class Education(models.Model):
    """Model for the education"""
    class Meta:
        verbose_name = "Education Model"
        verbose_name_plural = "Education Model"
    
    institution = models.CharField(max_length=50)
    level_choices = [
        ('Senior High School','Senior High School'),
        ('Undergraduate','Undergraduate'),
        ('Postgraduate','Postgraduate'),
    ]
    institution_level = models.CharField(max_length=100, choices=level_choices)
    graduation_date = models.DateField()
    grade = models.FloatField()
    institution_icon = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.institution



class Jobs(models.Model):
    """Model for the Jobs"""
    class Meta:
        verbose_name = "Jobs Model"
        verbose_name_plural = "Job Model"

    company_name = models.CharField(max_length=100)
    duration = models.DurationField()

    def __str__(self):
        return self.company_name


class Volunteer(models.Model):
    """Model for the Voluteer jobs"""
    class Meta:
        verbose_name = "Volunteer Model"
        verbose_name_plural = "Volunteer Model"


    volunteer_organization = models.CharField(max_length=100)
    year = models.DateField()

    def __str__(self):
        return self.volunteer_organization


class Publications(models.Model):
    """Model for the Publications"""

    class Meta:
        verbose_name = "Publications Model"
        verbose_name_plural = "Publications Model"
    
    title = models.CharField(max_length=100)
    year = models.DateField()
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Languages(models.Model):
    """Model for the Languages"""
    pass

    