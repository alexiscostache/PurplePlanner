# Generated by Django 3.1.6 on 2021-02-27 16:32

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(choices=[('ST', 'Student'), ('TR', 'Teacher'), ('PL', 'Principal'), ('VR', 'Visitor')], default='VR', max_length=15)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('descripition', models.TextField()),
                ('users', models.ManyToManyField(to='todo.MyUser')),
            ],
        ),
        migrations.CreateModel(
            name='Assignments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('descripition', models.TextField()),
                ('date_start', models.DateTimeField()),
                ('date_due', models.DateTimeField()),
                ('date_complete', models.DateTimeField()),
                ('progress', models.FloatField()),
                ('grade', models.FloatField()),
                ('importance', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(-1), django.core.validators.MaxValueValidator(100)])),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.courses')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.myuser')),
            ],
        ),
    ]
