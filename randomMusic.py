import requests
from random import *
from pydub import AudioSegment
from io import BytesIO
from urllib.request import urlopen
import database



def Get(chat_id):
	obj = database.mainAPI[chat_id]
	musicList = obj['tracks']['data'];
	r = randrange(len(musicList))

	song_name = musicList[r]['title']
	song_artist = musicList[r]['artist']['name']
	music_url = musicList[r]['preview']

	database.song_artist_list[chat_id] = song_artist
	database.song_name_list[chat_id] = song_name

	music = urlopen(music_url).read()
	sound = AudioSegment.from_mp3(BytesIO(music))
	duration = len(sound)
	need_len = min(duration, 20000)
	start_point = randint(0, duration - need_len)
	send_music = sound[start_point:start_point + need_len]

	return send_music;
