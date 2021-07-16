import telebot
import randomMusic
from pydub import AudioSegment
from random import *
from urllib.request import urlopen
from io import BytesIO
import urllib
import urllib.request


bot = telebot.TeleBot('1847617795:AAGC9PPTMvbl9FeoGG2-4gcywEgAB2PCYGE')

@bot.message_handler(commands=['start'])
def start_command(message):
	bot.send_message(message.chat.id, "Hello daun! Print /game for playing")
@bot.message_handler(commands=['game'])
def game_command(message):
  music_url = randomMusic.Get()
  music = urllib.request.urlopen(music_url).read()
  sound = AudioSegment.from_mp3(BytesIO(music))
  duration = len(sound)
  start_point = randint(0, duration - 10000)
  send_music = sound[start_point:start_point + 10000]
  bot.send_message(message.chat.id, "Processing music...")
  bot.send_audio(message.chat.id, send_music.export("Guess It!", format="mp3")
)


bot.polling()