# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-14 04:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project', '0003_auto_20171113_2048'),
        ('account', '0002_freelancer_skills'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dashboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Client')),
                ('freelancer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Freelancer')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Project')),
            ],
        ),
    ]
