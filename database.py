import requests

song_name_list = {}
song_artist_list = {}
score_array = {}

stopped = {}
already_started = {}

is_name_guessed = {}
is_artist_guessed = {}

AnimeAPI = requests.get('https://api.deezer.com/playlist/9284561822').json()
PopAPI = requests.get('https://api.deezer.com/playlist/9284561822').json()
OldAPI = requests.get('https://api.deezer.com/playlist/9284561822').json()

mainAPI = {}

def isAlreadyStarted(chat_id):
  if chat_id not in already_started:
    return 0
  return already_started[chat_id]


def isStopped(chat_id):
  if chat_id not in stopped:
    return 0
  return stopped[chat_id]

def clear_all(chat_id):
  already_started[chat_id] = 0
  stopped[chat_id] = 0
  song_name_list[chat_id] = ""
  song_artist_list[chat_id] = ""

def clear_current(chat_id):
  is_name_guessed[chat_id] = 0
  is_artist_guessed[chat_id] = 0

def found(chat_id):
  if chat_id not in is_name_guessed:
    return 0
  if chat_id not in is_artist_guessed:
    return 0
  return (is_name_guessed[chat_id] and is_artist_guessed[chat_id])

mainAPI = AnimeAPI
