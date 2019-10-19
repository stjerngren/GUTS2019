# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-10-19 00:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pill_today', models.BooleanField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pills_monday', models.BooleanField()),
                ('pills_tuesday', models.BooleanField()),
                ('pills_wednesday', models.BooleanField()),
                ('pills_thursday', models.BooleanField()),
                ('pills_friday', models.BooleanField()),
                ('pills_saturday', models.BooleanField()),
                ('pills_sunday', models.BooleanField()),
                ('pills_monday_amount', models.IntegerField()),
                ('pills_tuesday_amount', models.IntegerField()),
                ('pills_wednesday_amount', models.IntegerField()),
                ('pills_thursday_amount', models.IntegerField()),
                ('pills_friday_amount', models.IntegerField()),
                ('pills_saturday_amount', models.IntegerField()),
                ('pills_sunday_amount', models.IntegerField()),
                ('pills_monday_time', models.TimeField()),
                ('pills_tuesday_time', models.TimeField()),
                ('pills_wednesday_time', models.TimeField()),
                ('pills_thursday_time', models.IntegerField()),
                ('pills_friday_time', models.TimeField()),
                ('pills_saturday_time', models.TimeField()),
                ('pills_sunday_time', models.TimeField()),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='patient.Patient')),
            ],
        ),
    ]
