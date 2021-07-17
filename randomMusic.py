import requests
from random import *
from pydub import AudioSegment
from io import BytesIO
from urllib.request import urlopen
import database


obj = requests.get('https://api.deezer.com/playlist/9284561822').json()
musicList = obj['tracks']['data'];
# print(len(musicList));

def Get(chat_id):
	r = randrange(len(musicList))

	song_name = musicList[r]['title']
	song_artist = musicList[r]['artist']['name']
	music_url = musicList[r]['preview']

	database.song_artist_list[chat_id] = song_artist
	database.song_name_list[chat_id] = song_name

	music = urlopen(music_url).read()
	sound = AudioSegment.from_mp3(BytesIO(music))
	duration = len(sound)
	start_point = randint(0, duration - 15000)
	send_music = sound[start_point:start_point + 15000]

	return send_music;
