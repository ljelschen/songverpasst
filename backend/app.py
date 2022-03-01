
#Webserver
from flask import Flask, request, jsonify
from flask_cors import CORS
import json

#MySQL
from pypika import Query, Table, Field, Order
from connect import connectToMySQL, connectToSpotify
from getSongs import *


#select the stations table from the database
tbStations = Table('sations')

#select the songs tabe from the database
tbSongs = Table('songs')
tnPlayedAt = Table('playedAt')

#create app
app = Flask(__name__)

#app.debug = True
#allow cross origin requests
CORS(app, resources={r'/*': {'origins': '*'}})

#routes
@app.route("/")
def index():
    return "<p>Hello, World!</p>"

@app.route("/getStations", methods=['GET', 'POST'])
def getStations():
    #save the stations with a post request
    if request.method == 'POST':
        mydb, cursor = connectToMySQL()
        data = request.get_json()
        q = Query.into(tbStations).columns('name', 'type', 'url').insert(data.get('name'), data.get('type'),data.get('url'))
        q = str(q).replace('"', '`')
        cursor.execute(q)
        mydb.commit()
        cursor.close()
    """
    IMPROVE: make a better return value
    """
    return "<p>Stations!</p>"



@app.route("/getSongsByStation", methods=['GET'])
def getSongsByStation():
    if request.method == 'GET':
        if request.args['station'] != None:
            #select all songs from the database
            mydb, cursor = connectToMySQL()
            q = Query.from_(tbSongs).select('*').where(tbSongs.station == request.args['station']).orderby(tbSongs.time, order=Order.desc)
            q = str(q).replace('"', '`')
            cursor.execute(q)

            #return the songs as json
            returnValues = []
            '''
            IMPROVE: better Fetching.... 
            '''

            for song in cursor.fetchall():
                returnValues.append({
                    "id": song[0],
                    "date": song[1],
                    "time": song[2],
                    "station": song[3],
                    "artist": song[4],
                    "title": song[5],
                    "img": song[6],
                    "album": song[7],
                    "spotify": song[8],
                })
            cursor.close()
            return jsonify(returnValues)
        else:
            return "<p>No station defined!</p>"

@app.route("/getAllSongs", methods=['GET'])
def getAllSongs():
    if request.method == 'GET':
            mydb, cursor = connectToMySQL()
            q = Query.from_(tbSongs).join(tnPlayedAt).on(tbSongs.id == tnPlayedAt.songID).select('*').orderby(tnPlayedAt.time, order=Order.desc)
            q = str(q).replace('"', '`')
            cursor.execute(q)

            #return the songs as json
            returnValues = []
            '''
            IMPROVE: better Fetching.... 
            '''
            for song in cursor.fetchall():
                returnValues.append({
                    "id": song[0],
                    "artist": song[1],
                    "title": song[2],
                    "img": song[3],
                    "album": song[4],
                    "spotify": song[5],
                    "date": song[8],
                    "time": song[9],
                    "station": song[10],
                })
            cursor.close()
            return jsonify(returnValues)


@app.route("/reloadStations", methods=['GET'])
def reloadStations():
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
    saveSongsBremenX("Bremen 4", urlBremen4)
    return "<p>All Stations loaded</p>"

@app.route('/about', methods=['GET'])
def about():
    if request.method == 'GET':
        return 'The about page'

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="127.0.0.1", port=5000)