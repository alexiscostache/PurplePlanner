# Generated by Django 3.1.6 on 2021-02-27 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignments',
            name='date_complete',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]