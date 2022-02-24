
#Webserver
from flask import Flask, request
from flask_cors import CORS

#MySQL
from pypika import Query, Table, Field
from mysqlsetup import connectToMySQL
mydb, cursor = connectToMySQL()


tbStations = Table('sations')


app = Flask(__name__)
app.debug = True

CORS(app, resources={r'/*': {'origins': '*'}})

@app.route("/")
def index():
    return "<p>Hello, World!</p>"

@app.route("/getStations", methods=['GET', 'POST'])
def getStations():
    if request.method == 'POST':
        data = request.get_json()
        q = Query.into(tbStations).columns('name', 'type', 'url').insert(data.get('name'), data.get('type'),data.get('url'))
        q = str(q).replace('"', '`')
        cursor.execute(q)
        mydb.commit()

    


    return "<p>Stations!</p>"
    

