#MySQL
from mysql import connector
#Enviroment Variables
from dotenv import dotenv_values
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