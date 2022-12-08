#!/usr/bin/env python

from rest_framework import serializers

from bodzify_api.model.track.LibraryTrack import LibraryTrack
from bodzify_api.serializer.criteria.CriteriaSerializer import CriteriaResponseSerializer
from bodzify_api.serializer.playlist.PlaylistSerializer import PlaylistSerializer


class LibraryTrackSerializer(serializers.ModelSerializer):

    class Meta:
        model = LibraryTrack
        fields = [
            'uuid',
            'url',
            'filename',
            'fileExtension',
            "title", 
            "artist", 
            "album", 
            "genre", 
            "duration", 
            "rating", 
            "language", 
            "addedOn"]


    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


class LibraryTrackResponseSerializer(serializers.ModelSerializer):
    genre = CriteriaResponseSerializer()
    playlists = PlaylistSerializer(many=True)

    class Meta:
        model = LibraryTrack
        fields = [
            'uuid',
            'url',
            'filename',
            'fileExtension',
            "title",
            "artist",
            "album",
            "genre",
            "duration",
            "rating",
            "language",
            "playlists",
            "addedOn"]
