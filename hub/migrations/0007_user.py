# Generated by Django 3.0.7 on 2020-07-02 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0006_auto_20200623_1708'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('birthdate', models.DateField()),
            ],
        ),
    ]
