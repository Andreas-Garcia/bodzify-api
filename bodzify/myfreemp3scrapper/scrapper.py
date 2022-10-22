import datetime
import os
import requests
import json

import bodzify.myfreemp3scrapper.settings as myfreemp3ScrapperSettings

from bodzify.models import MineSong

def getSongsFromMyfreemp3Json (dataDict):
    songs = []
    for songJson in dataDict[myfreemp3ScrapperSettings.FIELD_DATA]:
        if songJson != "apple":
            songs.append(MineSong(
                title=songJson[myfreemp3ScrapperSettings.FIELD_TITLE], 
                artist=songJson[myfreemp3ScrapperSettings.FIELD_ARTIST], 
                duration=songJson[myfreemp3ScrapperSettings.FIELD_DURATION], 
                releasedOn=songJson[myfreemp3ScrapperSettings.FIELD_RELEASED_ON],
                url=songJson[myfreemp3ScrapperSettings.FIELD_URL]))
    return songs

def logResponseText (responseText):
    myfreemp3ScrapperLogFolderPath = myfreemp3ScrapperSettings.LOG_FOLDER_PATH
    
    if not os.path.exists(myfreemp3ScrapperLogFolderPath):
        os.makedirs(myfreemp3ScrapperLogFolderPath)

    logFileName = datetime.datetime.now().strftime(myfreemp3ScrapperSettings.LOG_FILE_NAME_FORMAT) + ".txt"
    f = open(myfreemp3ScrapperSettings.LOG_FOLDER_PATH + logFileName, "x")
    f.write(responseText)
    f.close()

def getJsonTextFromSongs (songs):
    songsJsonText = "["
    firstSong = True
    for song in songs:
        if firstSong: firstSong = False
        else: songsJsonText += ", "
        songsJsonText += json.dumps(song.__dict__)
    songsJsonText += "]"
    return songsJsonText

def getMyfreemp3ResponseJsonFromMyfreemp3ResponseText (myfreemp3ResponseJsonResponseText):
    myfreemp3songsJsonText = "{" + myfreemp3ResponseJsonResponseText.split("{",2)[2]
    myfreemp3songsJsonText = myfreemp3songsJsonText[:len(myfreemp3songsJsonText) - 4]
    return json.loads(myfreemp3songsJsonText)

def scrap (search, page):

    dataToSendToMyfreemp3 = {
        'q': search,
        'page': str(page)
    }
    
    responseText = requests.post(url = myfreemp3ScrapperSettings.POST_URL, data = dataToSendToMyfreemp3).text
    logResponseText(responseText)

    myfreemp3songsJson = getMyfreemp3ResponseJsonFromMyfreemp3ResponseText(responseText)
    songs = getSongsFromMyfreemp3Json(myfreemp3songsJson)
    songsJsonText = getJsonTextFromSongs(songs)
    return json.loads(songsJsonText)
    
