# Generated by Django 4.1 on 2022-10-21 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfreemp3api', '0009_alter_songdb_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songdb',
            name='uuid',
            field=models.UUIDField(unique=True),
        ),
    ]
