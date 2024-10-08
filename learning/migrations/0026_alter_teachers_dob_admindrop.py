# Generated by Django 5.0.1 on 2024-01-10 14:01

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0025_alter_teachers_dob_uploadedfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachers',
            name='dob',
            field=models.DateField(default=datetime.datetime(2024, 1, 10, 14, 1, 59, 118193)),
        ),
        migrations.CreateModel(
            name='admindrop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=255)),
                ('icon', models.CharField(default='', max_length=100)),
                ('parent_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='learning.admindrop')),
            ],
        ),
    ]
