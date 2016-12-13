# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-13 10:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(default='', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(upload_to='images/', verbose_name='Image')),
                ('description', models.CharField(blank=True, max_length=600, null=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
