# Generated by Django 3.0.7 on 2020-06-18 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_auto_20200618_1922'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addads',
            old_name='timepub',
            new_name='publish',
        ),
    ]