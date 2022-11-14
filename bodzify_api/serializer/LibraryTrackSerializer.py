#!/usr/bin/env python

from rest_framework import serializers

from bodzify_api.models import LibraryTrack
from bodzify_api.serializer.GenreSerializer import GenreRequestSerializer

class LibraryTrackSerializer(serializers.ModelSerializer):

    class Meta:
        model = LibraryTrack
        fields = [
            'uuid',
            'relativeUrl',
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
    genre = GenreRequestSerializer()

    def get_genreName(self, obj):
        if obj.genre is None:
            return None
        else:
            return obj.genre.name

    class Meta:
        model = LibraryTrack
        fields = [
            'uuid',
            'relativeUrl',
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