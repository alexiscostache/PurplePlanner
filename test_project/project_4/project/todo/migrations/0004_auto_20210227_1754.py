# Generated by Django 3.1.6 on 2021-02-27 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20210227_1752'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignments',
            old_name='descripition',
            new_name='description',
        ),
    ]
