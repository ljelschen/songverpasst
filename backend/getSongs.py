from bs4 import BeautifulSoup
import requests
import json
import datetime

#MySQL
from pypika import Query, Table, Field
from mysqlsetup import connectToMySQL
mydb, cursor = connectToMySQL()


date = datetime.date.today()

tbSongs = Table('songs')




def getAllSongs():
    q = Query.from_(tbSongs).select('*').orderby(tbSongs.time)
    q = str(q).replace('"', '`')
    cursor.execute(q)
    return cursor.fetchall()

def checkDuplicateSong(song):
    q = Query.from_(tbSongs).select('*').where(tbSongs.date == date).where(tbSongs.time == song['time']).where(tbSongs.interpret == song['interpret']).where(tbSongs.title == song['title'])
    q = str(q).replace('"', '`')
    cursor.execute(q)
    result = cursor.fetchall()
  
    if len(result) > 0:
        #return true if song is already in database
        return True
    else:
        #return fals if song is not in the  database
        return False

def saveSongsByTimeBremenX(station, searchTime, url, debug=False):
    #This does Work for Bremen 1, Bremen 2, Bremen 4, Bremen Next
    r = requests.get(url)
    if r.status_code == 200:
        soup = BeautifulSoup(r.content,"html.parser")
        for song in soup.find_all('tr')[1::]:
            time = song.find_all('td')[0].text.replace("\n","")
            interpret = song.find_all('td')[1].text.replace("\n","")
            title = song.find_all('td')[2].text.replace("\n","")
            print(checkDuplicateSong({'time': time, 'interpret': interpret, 'title': title}))
            if not debug and not checkDuplicateSong({'time': time, 'interpret': interpret, 'title': title}):
                q = Query.into(tbSongs).columns('date', 'time', 'station', 'interpret', 'title').insert(date, time, station, interpret, title)
                q = str(q).replace('"', '`')
                cursor.execute(q)
                mydb.commit()
    else:
        return None


url = "https://www.bremenvier.de/titelsuche-102~ajax.html?playlistsearch-searchDate=2022-02-24&playlistsearch-searchTime=18:10&_=1645722701763"
songs = saveSongsByTimeBremenX("Bremen 4", "18:10", url)
