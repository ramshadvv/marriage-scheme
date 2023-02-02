# Generated by Django 4.1.6 on 2023-02-01 20:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('dob', models.DateField(default=datetime.date(2023, 2, 2))),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('religion', models.CharField(blank=True, max_length=100, null=True)),
                ('job', models.CharField(blank=True, max_length=100, null=True)),
                ('annual_income', models.CharField(blank=True, max_length=100, null=True)),
                ('app_status', models.CharField(choices=[('Approved', 'Approved'), ('Denied', 'Denied')], default='Pending', max_length=100)),
            ],
        ),
    ]