# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-27 09:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jianshu', '0004_auto_20160724_0049'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articledetail',
            old_name='likes',
            new_name='likes_count',
        ),
        migrations.RenameField(
            model_name='articledetail',
            old_name='comments',
            new_name='public_comments_count',
        ),
        migrations.RenameField(
            model_name='articledetail',
            old_name='tip',
            new_name='total_rewards_count',
        ),
        migrations.RenameField(
            model_name='articledetail',
            old_name='views',
            new_name='views_count',
        ),
    ]
