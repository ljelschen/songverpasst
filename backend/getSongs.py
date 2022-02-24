#import data
from bs4 import BeautifulSoup
import requests
import json
import datetime
import time
#MySQL
from pypika import Query, Table, Field
from mysqlsetup import connectToMySQL
mydb, cursor = connectToMySQL()

#set the date to today
date = datetime.date.today()

#select the songs tabe from the database
tbSongs = Table('songs')

# read all songs from the database
def getAllSongs():
    q = Query.from_(tbSongs).select('*').orderby(tbSongs.time)
    q = str(q).replace('"', '`')
    cursor.execute(q)
    return cursor.fetchall()

#check for duplicates songs in the database
def checkDuplicateSong(song):
    q = Query.from_(tbSongs).select('*').where(tbSongs.date == date).where(tbSongs.date == song['date']).where(tbSongs.time == song['time']).where(tbSongs.interpret == song['interpret']).where(tbSongs.title == song['title'])
    q = str(q).replace('"', '`')
    cursor.execute(q)
    result = cursor.fetchall()
    if len(result) > 0:
        #return true if song is already in database
        return True
    else:
        #return fals if song is not in the  database
        return False




#### Bremen 4
def saveSongsBremen4(station, url, debug=False):
    #This does Work for Bremen 4
    r = requests.get(url)
    if r.status_code == 200:
        songs = []
        soup = BeautifulSoup(r.content,"html.parser")
        for song in soup.find_all('tr')[1::]:
            timeNow = song.find_all('td')[0].text.replace("\n","")
            interpret = song.find_all('td')[1].text.replace("\n","")
            title = song.find_all('td')[2].text.replace("\n","")
            #print(checkDuplicateSong({'time': time, 'interpret': interpret, 'title': title}))
            if not debug and not checkDuplicateSong({'date': date, 'time': timeNow, 'interpret': interpret, 'title': title}):
                q = Query.into(tbSongs).columns('date', 'time', 'station', 'interpret', 'title').insert(date, timeNow, station, interpret, title)
                q = str(q).replace('"', '`')
                cursor.execute(q)
                mydb.commit()
            songs.append({'date': date, 'time': timeNow, 'interpret': interpret, 'title': title})
        return songs
    else:
        return None

#reads the songs from the website via json and saves them to the database
def saveSongsBremenX(station, url):
    #This does Work for Bremen 1, Bremen 2, Bremen 4, Bremen Next
    result = requests.get(url)
    if result.status_code == 200:
        #convert to json
        json_data = json.loads(result.text)
        #get the songs
        songsRetrun = []
        songs = json_data['playlistPrevious']

        for song in songs:
            state = checkDuplicateSong({'date': date, 'time': song['time'], 'interpret': song['artist'], 'title': song['song']})
            if not state:
                q = Query.into(tbSongs).columns('date', 'time', 'station', 'interpret', 'title').insert(date, song['time'], station, song['artist'], song['song'])
                q = str(q).replace('"', '`')
                cursor.execute(q)
                mydb.commit()
            songsRetrun.append({'date': date, 'time': song['time'], 'interpret': song['artist'], 'title': song['song']})
        return songsRetrun
    else:
        return None
    

##### Json Abfrage
timestamp = str(int(round(time.time(), 0))) + '000'

#Bremen 1
urlBremen1 = f"https://www.bremeneins.de/startseite-bremen-eins-100~ajax_ajaxType-epg.json?_={timestamp}"
saveSongsBremenX("Bremen 1", urlBremen1)

#Bremen 2
urlBremen2 = f"https://www.bremenzwei.de/startseite-bremen-zwei-100~ajax_ajaxType-epg.json?_={timestamp}"
saveSongsBremenX("Bremen 2", urlBremen2)

#Bremen Next
urlBremenNext = f"https://www.bremennext.de/bremennext-startseite100~ajax_ajaxType-epg.json?_={timestamp}"
saveSongsBremenX("Bremen Next", urlBremenNext)

##### Speziale Abfrage

#Bremen 4
hour = datetime.datetime.now().hour
minute = datetime.datetime.now().minute
urlBremen4 = f"https://www.bremenvier.de/titelsuche-102~ajax.html?playlistsearch-searchDate={date}&playlistsearch-searchTime={hour}%3A{minute}"
saveSongsBremen4("Bremen 4", urlBremen4)



