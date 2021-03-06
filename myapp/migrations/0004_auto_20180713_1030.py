# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-13 10:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='place',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'place',
            },
        ),
        migrations.CreateModel(
            name='waiter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='restaurant',
            fields=[
                ('place', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='myapp.place')),
                ('juice', models.BooleanField()),
            ],
            options={
                'db_table': 'restaurant',
            },
        ),
        migrations.AddField(
            model_name='waiter',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.restaurant'),
        ),
    ]
