# Generated by Django 4.2.16 on 2024-11-05 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_resubmission'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resubmission',
            name='review',
        ),
    ]
