#MySQL
from mysql import connector
#Enviroment Variables
from dotenv import dotenv_values
#import spotify data
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

config = dotenv_values(".env")

def connectToMySQL():
  #connect to the database
  mydb = connector.connect(
    host=config['DB_HOST'],
    user=config['DB_USER'],
    password=config['DB_PASSWORD'],
    database=config['DB_DATABASE']
  )

  cursor = mydb.cursor()
  return mydb, cursor


def connectToSpotify():
  #connect to the database
  sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=config['SPOTIFY_CLIENT_ID'],
    client_secret=config['SPOTIFY_CLIENT_SECRET']
  ))
  return sp