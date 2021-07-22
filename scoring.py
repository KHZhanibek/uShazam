import database
import re
#asdas
def normalize(text):
  text = text.replace(' ', '')
  text = text.lower()

  nxt_text = ""
  found = 0
  for ch in text:
    if ch == '(':
      found = 1
    elif ch == ')':
      found = 0
    else:
      if found == 0 and ch.isalpha():
        nxt_text += ch
  return nxt_text

def isGuessed(user_text, need_next):
  if(user_text == need_next):
    return 1
  return 0

def getMask(chat_id, user_text):
  song_name = normalize(database.song_name_list[chat_id])
  song_artist = normalize(database.song_artist_list[chat_id])
  user_text = normalize(user_text)

  name_guessed = 0
  artist_guessed = 0

  if isGuessed(song_name, user_text) and database.is_name_guessed == 0:
    name_guessed = 1

  if isGuessed(song_artist, user_text) and database.is_artist_guessed == 0:
    artist_guessed = 1

  if name_guessed and artist_guessed:
    return 3
  if name_guessed:
    return 1
  if artist_guessed:
    return 2
  return 0

def getScore(user_text, name, chat_id, bot):
  if chat_id not in database.song_name_list:
    return

  if database.song_name_list[chat_id] == "":
    return

  if chat_id not in database.score_array:
    score_array[chat_id] = {}

  if name not in database.score_array[chat_id]:
    database.score_array[chat_id][name] = 0

  cur_msk = getMask(chat_id, user_text)

  if cur_msk == 1:
    bot.send_message(chat_id, "The name guessed!\n" + name + " gets 1 point!")
    database.is_name_guessed[chat_id] = 1
    database.score_array[chat_id][name] += 1
  if cur_msk == 2:
    bot.send_message(chat_id, "The aritst guessed!\n" + name + " gets 1 point!")
    database.is_artist_guessed[chat_id] = 1
    database.score_array[chat_id][name] += 1
  if cur_msk == 3:
    bot.send_message(chat_id, "Congratz! The name and artist guessed!\n" + name + " gets 3 points!")
    database.is_artist_guessed[chat_id] = database.is_name_guessed[chat_id] = 1
    database.score_array[chat_id][name] += 3
