# Generated by Django 3.2.5 on 2022-08-17 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0003_lesson_planned_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='planned_time',
            field=models.CharField(blank=True, max_length=164, null=True),
        ),
    ]