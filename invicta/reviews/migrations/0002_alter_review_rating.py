# Generated by Django 3.2.5 on 2022-08-18 23:18

from django.db import migrations, models
import reviews.models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.PositiveIntegerField(validators=[reviews.models.rating_validator]),
        ),
    ]
