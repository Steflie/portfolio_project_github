# Generated by Django 3.1.4 on 2021-01-05 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_app', '0007_volunteer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Publications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('year', models.DateField()),
                ('url', models.URLField(blank=True)),
            ],
            options={
                'verbose_name': 'Publications Model',
                'verbose_name_plural': 'Publications Model',
            },
        ),
    ]