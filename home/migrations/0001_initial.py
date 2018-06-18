# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-06-13 03:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoundPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sex', models.CharField(max_length=15)),
                ('FoundIn', models.CharField(max_length=150)),
                ('FoundDate', models.CharField(max_length=10)),
                ('Location', models.CharField(max_length=150)),
                ('Details', models.CharField(max_length=4000)),
                ('FoundPersonImage', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='MissingPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=40)),
                ('SecondName', models.CharField(max_length=40)),
                ('Sex', models.CharField(max_length=15)),
                ('AgeBeforeMissing', models.CharField(max_length=3)),
                ('DateOfBirth', models.CharField(max_length=10)),
                ('HairColour', models.CharField(max_length=50)),
                ('EyesColour', models.CharField(max_length=50)),
                ('Weight', models.CharField(max_length=4)),
                ('Height', models.CharField(max_length=4)),
                ('MissingFrom', models.CharField(max_length=150)),
                ('MissingDate', models.CharField(max_length=10)),
                ('RelativeID', models.CharField(max_length=15)),
                ('RelativeRelation', models.CharField(max_length=80)),
                ('Details', models.CharField(max_length=4000)),
                ('MissingPersonImage', models.CharField(max_length=2000)),
            ],
        ),
    ]