#import data
from bs4 import BeautifulSoup
import requests
import json
import datetime
import time
#include the MySQL settings
from pypika import Query, Table, Field
from connect import connectToMySQL, connectToSpotify

sp = connectToSpotify()


def getSongInfo(artist, title):
    #search qurry
    q = f"{artist} {title}"
    #request the search
    results = sp.search(q= q, limit=1)
    if results['tracks']['total'] > 0:
        track = results['tracks']['items'][0]
        ## return the img, album, url
        return track['album']['images'][0]['url'], track['album']['name'], track['uri']



mydb, cursor = connectToMySQL()

#set the date to today
date = datetime.date.today()

#select the songs tabe from the database
tbSongs = Table('songs')

# read all songs from the database
def getAllSongs():
    """
    PERFORMANCE: This function can be slow. Maybe select only the songs from the current day.
    """
    q = Query.from_(tbSongs).select('*').orderby(tbSongs.time)
    q = str(q).replace('"', '`')
    cursor.execute(q)
    return cursor.fetchall()

#check for duplicates songs in the database
def checkDuplicateSong(song):
    """
    PERFORMANCE: This function can be slow. Maybe we can improve it.
    """
    #check for duplicates songs in the database
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
    #wehn the request is successful
    if r.status_code == 200:
        #variable for the return value
        songs = []
        #extraxt the html content fom the response
        soup = BeautifulSoup(r.content,"html.parser")
        #search for the table rows in the html
        """
        FUTURE: could be buggy if the website changes
        """
        for song in soup.find_all('tr')[1::]:
            #extract the song from the html table
            timeNow = song.find_all('td')[0].text.replace("\n","")
            interpret = song.find_all('td')[1].text.replace("\n","")
            title = song.find_all('td')[2].text.replace("\n","")
            #check for duplicates
            if not debug and not checkDuplicateSong({'date': date, 'time': timeNow, 'interpret': interpret, 'title': title}):
                #save the song to the database
                q = Query.into(tbSongs).columns('date', 'time', 'station', 'interpret', 'title').insert(date, timeNow, station, interpret, title)
                q = str(q).replace('"', '`')
                cursor.execute(q)
                mydb.commit()
            #add the song to the return value
            songs.append({'date': date, 'time': timeNow, 'interpret': interpret, 'title': title})
        #return the songs
        return songs
    else:
        return None

#reads the songs from the website via json and saves them to the database
def saveSongsBremenX(station, url):
    #This does Work for Bremen 1, Bremen 2, Bremen 4, Bremen Next
    result = requests.get(url)
    #wehn the request is successful
    if result.status_code == 200:
        #convert to json
        json_data = json.loads(result.text)
        #get the songs from the json object
        songs = json_data['playlistPrevious']
        #variable for the return value
        songsRetrun = []
        #loop through the songs
        for song in songs:
            if not checkDuplicateSong({'date': date, 'time': song['time'], 'interpret': song['artist'], 'title': song['song']}):
            
                #replace " mit" durch "," um ein besseren erfolg bei der Spotify Suche zu erzielen
                if "mit " in song['artist']:
                    song['artist'] = song['artist'].replace(" mit", ",")
     
                #get Song info
                info = getSongInfo(song['artist'], song['song'])
                if info != None:
                    img, album, spotifyUrl = info
                 #save the song to the database
                    q = Query.into(tbSongs).columns('date', 'time', 'station', 'interpret', 'title', 'img', 'album', 'spotify').insert(date, song['time'], station, song['artist'], song['song'], img, album, spotifyUrl )
                    q = str(q).replace('"', '`')
                    cursor.execute(q)
                    mydb.commit()
                else:
                    q = Query.into(tbSongs).columns('date', 'time', 'station', 'interpret', 'title', 'img', 'album', 'spotify').insert(date, song['time'], station, song['artist'], song['song'], "", "", "")
                    q = str(q).replace('"', '`')
                    cursor.execute(q)
                    mydb.commit()
      
            #add the song to the return value
            songsRetrun.append({'date': date, 'time': song['time'], 'interpret': song['artist'], 'title': song['song']})
        #return all songs
        return songsRetrun
    else:
        return None
    
if __name__ == "__main__":
    ##### Json Abfrage
    #create a timesamp in the formart of the bremen website
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

    #Bremen 4
    urlBremen4 = f"https://www.bremenvier.de/bremenvier-startseite100~ajax_ajaxType-epg.json?_={timestamp}"
    saveSongsBremenX("Bremen 4", urlBremenNext)



