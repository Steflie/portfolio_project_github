# Generated by Django 3.1.4 on 2021-01-05 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_app', '0002_auto_20210105_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='institution_icon',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]