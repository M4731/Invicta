# Generated by Django 3.2.5 on 2022-08-09 16:59

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
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField()),
                ('time', models.CharField(choices=[('8-10', '08:00-10:00'), ('10-12', '10:00-12:00'), ('12-14', '12:00-14:00'), ('14-16', '14:00-16:00'), ('16-18', '16:00-18:00'), ('18-20', '18:00-20:00'), ('20-22', '20:00-22:00')], max_length=5)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.teacher')),
            ],
            options={
                'ordering': ['day', 'time'],
                'unique_together': {('teacher', 'day', 'time')},
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Basic Lesson', max_length=264)),
                ('program', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lessons.program')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.teacher')),
            ],
        ),
    ]
