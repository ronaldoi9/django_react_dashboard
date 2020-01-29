# Generated by Django 3.0.2 on 2020-01-25 17:28

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200125_1714'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatesAndCities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initials', models.CharField(max_length=2)),
                ('state', models.CharField(max_length=25)),
                ('cities', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=60), default=list, size=None)),
            ],
        ),
    ]