# Generated by Django 3.0.7 on 2020-06-23 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0004_auto_20200622_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='stamp',
            name='title',
            field=models.CharField(default=models.CharField(max_length=20), max_length=50),
        ),
    ]
