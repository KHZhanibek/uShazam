import database
import time
import randomMusic
from telebot import types

def checkGenre(message, chat_id):
  if message.text == 'Anime Music':
    database.mainAPI[chat_id] = database.AnimeAPI
    return getRoundsButtons()
  if message.text == 'Pop Music':
    database.mainAPI[chat_id] = database.PopAPI
    return getRoundsButtons()
  if message.text == 'Old Music':
    database.mainAPI[chat_id] = database.OldAPI
    return getRoundsButtons()
  return 0;


def checkRounds(message):
  if message.text == '10 rounds':
    return 10
  elif message.text == '15 rounds':
    return 15
  elif message.text == '20 rounds':
    return 20
  elif message.text == 'Eternal Tsukuyomi':
    return 1000000000
  else:
    return 0

def getGenreButtons():

  genreList = types.ReplyKeyboardMarkup(resize_keyboard = True)

  pop = types.KeyboardButton(text = 'Pop Music')
  anime = types.KeyboardButton(text = 'Anime Music')
  old = types.KeyboardButton(text = 'Old Music')

  genreList.add(pop, anime, old);

  return genreList


def getRoundsButtons():

  roundsList = types.ReplyKeyboardMarkup(resize_keyboard = True)

  roundType1 = types.KeyboardButton(text = '10 rounds')
  roundType2 = types.KeyboardButton(text = '15 rounds')
  roundType3 = types.KeyboardButton(text = '20 rounds')
  roundType4 = types.KeyboardButton(text = 'Eternal Tsukuyomi')

  roundsList.add(roundType1, roundType2, roundType3, roundType4)

  return roundsList

def Rounds(rounds):
  pass


def startGame(bot, round_number, chat_id):
  database.score_array[chat_id] = {}
  database.already_started[chat_id] = 1

  for round in range(round_number):
    start_time = time.time()

    bot.send_message(chat_id, "Round " + str(round + 1) + "/" + str(round_number) + "\n▶️ Processing music...")
    send_music = randomMusic.Get(chat_id)
    bot.send_audio(chat_id, send_music.export("Guess It!", format="mp3"))
    database.clear_current(chat_id)

    while time.time() - start_time < 30.0:
      if database.found(chat_id) or database.stopped:
        break

    if database.stopped:
      break

    bot.send_message(chat_id, "It is " + database.song_name_list[chat_id] + " : " + database.song_artist_list[chat_id])


  database.clear_all(chat_id)
