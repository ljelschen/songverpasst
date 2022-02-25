from bs4 import BeautifulSoup
import requests


url = "https://www1.wdr.de/radio/1live/musik/playlist/index.jsp"
r = requests.get(url)
soup = BeautifulSoup(r.content,"html.parser")
table = soup.find_all('table', class_="thleft")[0]
songs = table.find_all('tr', class_="data")[1::]

for song in songs:

    
    print(song.find('td', class_="entry datetime"))
    print(song.find('td', class_="entry performer").text.replace("\n",""))
    print(song.find('td', class_="entry title").text.replace("\n",""))

