# Generated by Django 3.0.2 on 2020-01-24 22:25

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='culinary',
            name='dishes',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=60), default='{}', size=None),
        ),
    ]