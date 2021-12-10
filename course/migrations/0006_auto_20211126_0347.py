# Generated by Django 3.2.9 on 2021-11-26 03:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_complain_action_taken'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='class',
            name='start_time',
        ),
        migrations.RemoveField(
            model_name='semester',
            name='class_running_period',
        ),
        migrations.RemoveField(
            model_name='semester',
            name='class_setup_period',
        ),
        migrations.AddField(
            model_name='class',
            name='end_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='class',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='semester',
            name='end_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='semester',
            name='registration_period',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='semester',
            name='running_period',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='semester',
            name='setup_period',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='semester',
            name='start_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='semester',
            name='grading_period',
            field=models.DateTimeField(),
        ),
    ]
