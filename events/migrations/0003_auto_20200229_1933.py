# Generated by Django 3.0.2 on 2020-02-29 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20200228_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='team_size',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
