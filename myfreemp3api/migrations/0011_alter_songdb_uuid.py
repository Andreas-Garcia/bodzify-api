# Generated by Django 4.1 on 2022-10-21 10:45

from django.db import migrations, models
import shortuuid.main


class Migration(migrations.Migration):

    dependencies = [
        ('myfreemp3api', '0010_alter_songdb_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songdb',
            name='uuid',
            field=models.UUIDField(default=shortuuid.main.ShortUUID.uuid, unique=True),
        ),
    ]
