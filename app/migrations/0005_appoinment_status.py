# Generated by Django 5.0.6 on 2024-06-19 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_appoinment_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='appoinment',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('accept', 'Accept'), ('Reject', 'Reject')], default=('pending', 'Pending'), max_length=100),
        ),
    ]
