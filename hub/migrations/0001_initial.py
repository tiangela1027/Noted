# Generated by Django 3.0.7 on 2020-06-22 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stamp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mood', models.CharField(max_length=20, unique=True)),
                ('notes', models.CharField(max_length=264, unique=True)),
                ('noteId', models.IntegerField()),
            ],
        ),
    ]
