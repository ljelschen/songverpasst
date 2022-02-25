
#Webserver
from flask import Flask, request, jsonify
from flask_cors import CORS
import json

#MySQL
from pypika import Query, Table, Field
from mysqlsetup import connectToMySQL
mydb, cursor = connectToMySQL()

#select the stations table from the database
tbStations = Table('sations')

#select the songs tabe from the database
tbSongs = Table('songs')

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
        data = request.get_json()
        q = Query.into(tbStations).columns('name', 'type', 'url').insert(data.get('name'), data.get('type'),data.get('url'))
        q = str(q).replace('"', '`')
        cursor.execute(q)
        mydb.commit()
    """
    IMPROVE: make a better return value
    """
    return "<p>Stations!</p>"



@app.route("/getSongsByStation", methods=['GET'])
def getSongsByStation():
    station = request.args['station']
    if station != None:
        #select all songs from the database
        q = Query.from_(tbSongs).select('*').where(tbSongs.station == station).orderby(tbSongs.time)
        q = str(q).replace('"', '`')
        cursor.execute(q)
        #return the songs as json
        returnValues = []
        for song in cursor.fetchall():
            returnValues.append({
                "id": song[0],
                "date": song[1],
                "time": song[2],
                "station": song[3],
                "artist": song[4],
                "title": song[5],
            })
        return jsonify(returnValues)
    else:
        return "<p>No station defined!</p>"
 
