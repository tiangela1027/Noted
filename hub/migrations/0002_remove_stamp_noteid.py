# Generated by Django 3.0.7 on 2020-06-22 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stamp',
            name='noteId',
        ),
    ]
