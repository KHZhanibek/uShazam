import telebot
import randomMusic
from pydub import AudioSegment
from random import *
from io import BytesIO
from urllib.request import urlopen


bot = telebot.TeleBot('1847617795:AAGC9PPTMvbl9FeoGG2-4gcywEgAB2PCYGE')

@bot.message_handler(commands=['start'])
def start_command(message):
	bot.send_message(message.chat.id, "Hello daun! Print /game for playing")
@bot.message_handler(commands=['game'])
def game_command(message):
  music_url = randomMusic.Get()
  music = urlopen(music_url).read()
  # print(music);
  sound = AudioSegment.from_mp3(BytesIO(music))
  duration = len(sound)
  start_point = randint(0, duration - 15000)
  send_music = sound[start_point:start_point + 15000]
  bot.send_message(message.chat.id, "Processing music...")
  bot.send_audio(message.chat.id, send_music.export("Guess It!", format="mp3"))


bot.polling()

# from urllib.request import urlopen

# html = urlopen("http://www.google.com/")
# print(html.read())