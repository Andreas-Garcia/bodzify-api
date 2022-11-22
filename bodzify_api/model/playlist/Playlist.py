#!/usr/bin/env python

import shortuuid

from django.db import models
from django.contrib.auth.models import User

class Playlist(models.Model):
    uuid = models.CharField(primary_key=True, default=shortuuid.uuid, max_length=200, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(unique=True, default=shortuuid.uuid, max_length=200, editable=False)
    addedOn = models.DateTimeField(auto_now_add=True)

class Meta:
        managed = False
        db_table = 'bodzify_api_playlist'