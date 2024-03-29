# Generated by Django 4.1.6 on 2023-02-02 05:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='dateapplied',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='application',
            name='app_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Denied', 'Denied')], default='Pending', max_length=100),
        ),
        migrations.AlterField(
            model_name='application',
            name='dob',
            field=models.DateField(),
        ),
    ]
