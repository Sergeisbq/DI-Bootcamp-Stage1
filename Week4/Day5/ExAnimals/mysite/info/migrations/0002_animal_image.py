# Generated by Django 4.2 on 2023-04-23 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
    ]
