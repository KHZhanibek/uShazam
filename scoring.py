import database

def IsGuessed(user_text, need_next):
#  Removing text in (brakets)
  start = need_next.find("(")
  end = need_next.find(")")
  if start != -1 and end != -1:
    need_next = need_next[start+1:end]
#-------------------------------------
  user_text = user_text.replace(' ', '')
  user_text = user_text.lower()
  need_next = need_next.replace(' ', '')
  need_next = need_next.lower()
  if user_text == need_next:
    return 1
  return 0

def SetScore(chat_id, user_text):
  song_name = database.song_name_list[chat_id]
  song_artist = database.song_artist_list[chat_id]
  score = 0;
  if(IsGuessed(song_name + song_artist, user_text)):
    score = 3
  if(IsGuessed(song_artist + song_name, user_text)):
    score = 3
  if(IsGuessed(song_name, user_text)):
    score = 1
  if(IsGuessed(song_artist, user_text)):
    score = 1
  return score;

def GetScore(user_text, name, chat_id):
  if chat_id not in database.song_name_list:
    return "No music given"

  if name not in database.score_array:
    database.score_array[name] = 0

  current_point = SetScore(chat_id, user_text)
  database.score_array[name] += current_point
  winner = ("You get " + str(current_point) + " points!")

  tot = ""
  for key in database.score_array:
    tot = tot +  key + ' has ' + str(database.score_array[key]) + " points\n"
  return (winner + "\n\n\n" + tot)