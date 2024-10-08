# Generated by Django 5.0.1 on 2024-02-08 18:12

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0122_alter_leave_today_alter_teacher_shifts_half_daytime_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='schoolid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='learning.schools'),
        ),
        migrations.AlterField(
            model_name='leave',
            name='today',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 8, 18, 12, 20, 47023)),
        ),
        migrations.AlterField(
            model_name='student',
            name='username',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='teacher_shifts',
            name='half_daytime',
            field=models.TimeField(verbose_name=datetime.datetime(2024, 2, 8, 18, 12, 20, 427)),
        ),
        migrations.AlterField(
            model_name='teacher_shifts',
            name='in_time',
            field=models.TimeField(verbose_name=datetime.datetime(2024, 2, 8, 18, 12, 20, 427)),
        ),
        migrations.AlterField(
            model_name='teacher_shifts',
            name='late_mark_time',
            field=models.TimeField(verbose_name=datetime.datetime(2024, 2, 8, 18, 12, 20, 427)),
        ),
        migrations.AlterField(
            model_name='teacher_shifts',
            name='out_time',
            field=models.TimeField(verbose_name=datetime.datetime(2024, 2, 8, 18, 12, 20, 427)),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='dob',
            field=models.DateField(default=datetime.datetime(2024, 2, 8, 18, 12, 20, 427)),
        ),
    ]
