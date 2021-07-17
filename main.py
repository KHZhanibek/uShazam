import telebot
import randomMusic
import scoring
import database


bot = telebot.TeleBot('1847617795:AAGC9PPTMvbl9FeoGG2-4gcywEgAB2PCYGE')

@bot.message_handler(commands=['start'])
def start_command(message):
  bot.send_message(message.chat.id, "Hello daun! Print /game for playing")

@bot.message_handler(commands=['game'])
def game_command(message):
  chat_id = message.chat.id
  bot.send_message(chat_id, "Processing music...")
  send_music = randomMusic.Get()
  bot.send_audio(chat_id, send_music.export("Guess It!", format="mp3"))

@bot.message_handler(content_types=['text'])
def GetScore(message):
  res = scoring.GetScore(message.text, message.from_user.first_name, message.chat.id)
  bot.send_message(message.chat.id, res);


bot.polling()
