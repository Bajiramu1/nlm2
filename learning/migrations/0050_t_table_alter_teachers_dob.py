# Generated by Django 5.0.1 on 2024-01-22 17:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0049_alter_teachers_dob'),
    ]

    operations = [
        migrations.CreateModel(
            name='t_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.CharField(max_length=10)),
                ('end_time', models.CharField(max_length=10)),
                ('period_time', models.PositiveIntegerField()),
                ('reces_break1', models.PositiveIntegerField()),
                ('reces_break2', models.PositiveIntegerField(default=None)),
                ('lunch_break', models.PositiveIntegerField()),
                ('w_break1', models.IntegerField(default=None)),
                ('w_break2', models.IntegerField(default=None)),
                ('w_lunch', models.IntegerField(default=None)),
            ],
        ),
        migrations.AlterField(
            model_name='teachers',
            name='dob',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 22, 17, 3, 48, 957004)),
        ),
    ]
