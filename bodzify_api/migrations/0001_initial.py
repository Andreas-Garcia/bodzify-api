# Generated by Django 4.1 on 2022-11-29 17:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import shortuuid.main


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Criteria',
            fields=[
                ('uuid', models.CharField(default=shortuuid.main.ShortUUID.uuid, editable=False, max_length=200, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('addedOn', models.DateTimeField(auto_now_add=True)),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='bodzify_api.criteria')),
            ],
        ),
        migrations.CreateModel(
            name='CriteriaType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(default=None, max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('uuid', models.CharField(default=shortuuid.main.ShortUUID.uuid, editable=False, max_length=200, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=None, default=None, max_length=200)),
                ('addedOn', models.DateTimeField(auto_now_add=True)),
                ('criteria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bodzify_api.criteria')),
            ],
        ),
        migrations.CreateModel(
            name='PlaylistType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(default=shortuuid.main.ShortUUID.uuid, editable=False, max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='GenrePlaylist',
            fields=[
                ('playlist_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bodzify_api.playlist')),
            ],
            bases=('bodzify_api.playlist',),
        ),
        migrations.CreateModel(
            name='TagPlaylist',
            fields=[
                ('playlist_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bodzify_api.playlist')),
            ],
            bases=('bodzify_api.playlist',),
        ),
        migrations.AddField(
            model_name='playlist',
            name='type',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='bodzify_api.playlisttype'),
        ),
        migrations.AddField(
            model_name='playlist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='LibraryTrack',
            fields=[
                ('path', models.CharField(max_length=200)),
                ('uuid', models.CharField(default=shortuuid.main.ShortUUID.uuid, editable=False, max_length=200, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('artist', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('album', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('duration', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('rating', models.IntegerField(blank=True, default=None, null=True)),
                ('language', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('addedOn', models.DateTimeField(auto_now_add=True)),
                ('genre', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='bodzify_api.criteria')),
                ('playlists', models.ManyToManyField(to='bodzify_api.playlist')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='criteria',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bodzify_api.criteriatype'),
        ),
        migrations.AddField(
            model_name='criteria',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='criteria',
            unique_together={('user', 'name', 'type', 'parent')},
        ),
    ]
