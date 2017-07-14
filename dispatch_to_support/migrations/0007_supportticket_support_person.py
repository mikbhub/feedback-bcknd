# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-13 15:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dispatch_to_support', '0006_auto_20170712_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='supportticket',
            name='support_person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]