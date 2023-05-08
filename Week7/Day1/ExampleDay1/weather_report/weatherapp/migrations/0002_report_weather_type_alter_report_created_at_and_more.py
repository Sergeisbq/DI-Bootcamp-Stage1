# Generated by Django 4.2.1 on 2023-05-08 10:09

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('weatherapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='weather_type',
            field=models.CharField(blank=True, choices=[('rainy', 'Rainy'), ('storm', 'Storm'), ('sunny', 'Sunny'), ('cloudy', 'Cloudy')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='location',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='report',
            name='temperature',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(-90.0), django.core.validators.MaxValueValidator(60.0)]),
        ),
        migrations.CreateModel(
            name='Forecaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forecaster_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='report',
            name='forecaster',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='weatherapp.forecaster'),
        ),
    ]
