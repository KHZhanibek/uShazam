import requests
from random import randrange


obj = requests.get('https://api.deezer.com/playlist/1282483245').json()
musicList = obj['tracks']['data'];
# print(len(musicList));

def Get():
	r = randrange(len(musicList))
	song_name = musicList[r]['title']
	song_artist = musicList[r]['artist']['name']
	return (musicList[r]['preview'], song_artist, song_name)
