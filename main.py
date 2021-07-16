import telebot
import scoring
import randomMusic
from pydub import AudioSegment
from random import *
from io import BytesIO
from urllib.request import urlopen


bot = telebot.TeleBot('1847617795:AAGC9PPTMvbl9FeoGG2-4gcywEgAB2PCYGE')

song_name_list = {}
song_artist_list = {}
score_array = {}


@bot.message_handler(commands=['start'])
def start_command(message):
	bot.send_message(message.chat.id, "Hello daun! Print /game for playing")

def SetScore(chat_id, user_text):
  song_name = song_name_list[chat_id]
  song_artist = song_artist_list[chat_id]

  if(scoring.IsGuessed(song_name + song_artist, user_text)):
    return 3
  if(scoring.IsGuessed(song_artist + song_name, user_text)):
    return 3
  if(scoring.IsGuessed(song_name, user_text)):
    return 1
  if(scoring.IsGuessed(song_artist, user_text)):
    return 1
  return 0

@bot.message_handler(commands=['game'])
def game_command(message):
  chat_id = message.chat.id

  music_url, song_artist, song_name = randomMusic.Get()
  music = urlopen(music_url).read()

  song_artist_list[chat_id] = song_artist
  song_name_list[chat_id] = song_name

  sound = AudioSegment.from_mp3(BytesIO(music))
  duration = len(sound)
  start_point = randint(0, duration - 15000)
  send_music = sound[start_point:start_point + 15000]

  bot.send_message(message.chat.id, "Processing music...")
  bot.send_audio(message.chat.id, send_music.export("Guess It!", format="mp3"))
  bot.send_message(message.chat.id, "Hint: " + song_artist + ":" + song_name)


@bot.message_handler(content_types=['text'])
def GetScore(message):
  user_text = message.text
  name = message.from_user.first_name
  chat_id = message.chat.id

  if chat_id not in song_name_list:
    bot.send_message(message.chat.id, "No music given")
    return

  if name not in score_array:
    score_array[name] = 0

  current_point = SetScore(chat_id, user_text)
  score_array[name] += current_point
  bot.send_message(message.chat.id, "You get " + str(current_point) + " points!")

  tot = ""
  for key in score_array:
    tot = tot +  key + ' has ' + str(score_array[key]) + " points\n"

  bot.send_message(message.chat.id, tot)


bot.polling()
