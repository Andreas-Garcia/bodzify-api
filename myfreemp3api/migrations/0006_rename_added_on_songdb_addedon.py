# Generated by Django 4.1 on 2022-10-20 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myfreemp3api', '0005_songdb_language'),
    ]

    operations = [
        migrations.RenameField(
            model_name='songdb',
            old_name='added_on',
            new_name='addedOn',
        ),
    ]
