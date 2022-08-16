# Generated by Django 3.2.5 on 2022-08-15 18:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sent_date', models.DateField(auto_now_add=True)),
                ('accepted', models.BooleanField(default=False)),
                ('planned_date', models.DateField(blank=True, null=True)),
                ('description', models.TextField()),
                ('time_description', models.TextField(default='Sunt liber oricand.')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.teacher')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-sent_date'],
            },
        ),
    ]
