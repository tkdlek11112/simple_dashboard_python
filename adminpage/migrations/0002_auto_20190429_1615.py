# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-04-29 07:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminpage', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Candidate',
            new_name='Faq',
        ),
    ]