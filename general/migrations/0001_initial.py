# Generated by Django 5.1.2 on 2024-10-18 00:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField()),
                ('identifier', models.TextField(default='_UniqueName_<django.db.models.fields.CharField>_2024-10-18 00:46:55.912657+00:00')),
                ('link', models.TextField()),
                ('published_date', models.TimeField(default=datetime.datetime(2024, 10, 18, 0, 46, 55, 912657, tzinfo=datetime.timezone.utc))),
            ],
        ),
    ]