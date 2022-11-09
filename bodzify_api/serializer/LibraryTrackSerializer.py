#!/usr/bin/env python

from rest_framework import serializers

from bodzify_api.models import LibraryTrack

import logging

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
    genreName = serializers.SerializerMethodField()

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
            "genreName", 
            "duration", 
            "rating", 
            "language", 
            "addedOn"]

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)