from django.db import models

# Create your models here.

class Education(models.Model):
    

    class Meta:
        verbose_name = "Education Model"
        verbose_name_plural = "Education Model"


    institution = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    study_field = models.CharField(max_length=100)
    grade = models.FloatField(blank=True)
    start_date = models.DateField(blank=True, null=True)
    finish_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.institution


class Jobs(models.Model):
    

    class Meta:
        verbose_name = "Job Model"
        verbose_name_plural = "Job Model"


    company_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=100)
    start_date = models.DateField()
    finish_date = models.DateField()
    description = models.TextField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    

    def __str__(self):
        return self.company_name


class Volunteer(models.Model):
    

    class Meta:
        verbose_name = "Volunteer Model"
        verbose_name_plural = "Volunteer Model"

    organization_name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    finish_date = models.DateField()
    program_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    
    def __str__(self):
        return self.organization_name


class Publications(models.Model):


    class Meta:
        verbose_name = "Publication Model"
        verbose_name_plural = "Publication Model"

    
    publication_title = models.CharField(max_length=100)
    publication_year = models.DateField()
    description = models.TextField()
    url = models.URLField(blank=True)

    def __str__(self):
        return self.publication_title


class Languages(models.Model):
    

    class Meta:
        verbose_name = "Language Model"
        verbose_name_plural = "Language Model"

    
    language = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    

    def __str__(self):
        return self.language