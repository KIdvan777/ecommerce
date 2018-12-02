# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-11-30 09:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20181129_1428'),
    ]

    operations = [
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='app',
            name='social_links',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.Social'),
            preserve_default=False,
        ),
    ]
