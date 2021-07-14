import requests
from random import randrange

obj = requests.get('https://api.deezer.com/playlist/1282483245').json()
musicList = obj['tracks']['data'];
# print(len(musicList));

def Get():
	r = randrange(len(musicList))
	return musicList[r]['preview']

Get()
# def get() :


