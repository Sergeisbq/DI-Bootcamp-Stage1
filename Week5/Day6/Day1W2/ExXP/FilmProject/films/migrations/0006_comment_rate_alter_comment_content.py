# Generated by Django 4.2.1 on 2023-05-07 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0005_alter_comment_author_alter_film_release_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='rate',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
