# Generated by Django 3.1.6 on 2021-02-28 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_assignments_attemps'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courses',
            old_name='descripition',
            new_name='description',
        ),
    ]
