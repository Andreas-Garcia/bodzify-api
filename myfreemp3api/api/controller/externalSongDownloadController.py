import os
import requests

import eyed3

import myfreemp3api.settings as apiSettings
from myfreemp3api.models import SongDB

def downloadExternalSong (user, song):
    userLibraryPath = apiSettings.LIBRARIES_PATH + user.get_username() + "/"

    if not os.path.exists(userLibraryPath):
        os.makedirs(userLibraryPath)

    externalSongUrl = song.url
    externalSong = requests.get(externalSongUrl)
    externalSongName, externalSongExtension = os.path.splitext(externalSongUrl)

    internalSongFilePathWithoutExtension = userLibraryPath + song.artist + " - " + song.title
    internalSongFilePath = internalSongFilePathWithoutExtension + externalSongExtension

    existingFileCount = 0
    while os.path.exists(internalSongFilePath):
        existingFileCount = existingFileCount + 1
        internalSongFilePath = internalSongFilePathWithoutExtension + " (" + str(existingFileCount) + ")" + externalSongExtension


    with open(internalSongFilePath, 'wb') as file:
        file.write(externalSong.content)
    
    songfile = eyed3.load(internalSongFilePath)
    songTags = songfile.tag
    songDB = SongDB(path=internalSongFilePath, 
        user=user, 
        title=songTags.title, 
        artist=songTags.artist, 
        album=songTags.album, 
        genre=songTags.genre, 
        duration=songfile.info.time_secs, 
        rating=songTags.popularities.get("rating"))
    songDB.save()
