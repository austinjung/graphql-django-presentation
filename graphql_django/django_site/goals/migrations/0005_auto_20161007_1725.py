# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-07 17:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0004_remove_objective_progress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='objective',
            name='state',
        ),
        migrations.AlterField(
            model_name='keyresult',
            name='objective',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='key_results', to='goals.Objective'),
        ),
        migrations.AlterField(
            model_name='objective',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='objectives', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]