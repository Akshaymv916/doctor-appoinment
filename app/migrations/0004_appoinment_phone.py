# Generated by Django 5.0.6 on 2024-06-19 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_appoinment'),
    ]

    operations = [
        migrations.AddField(
            model_name='appoinment',
            name='phone',
            field=models.IntegerField(default=0),
        ),
    ]
