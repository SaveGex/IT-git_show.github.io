# Generated by Django 5.1.2 on 2024-10-18 02:34

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='identifier',
        ),
        migrations.AlterField(
            model_name='posts',
            name='description',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='posts',
            name='published_date',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
