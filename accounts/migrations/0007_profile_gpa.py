# Generated by Django 3.2.9 on 2021-11-25 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_application_rejected'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='GPA',
            field=models.FloatField(default=0.0),
        ),
    ]
