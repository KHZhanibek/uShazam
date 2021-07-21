import telebot
import randomMusic
import scoring
import database
import controller

bot = telebot.TeleBot('1847617795:AAGC9PPTMvbl9FeoGG2-4gcywEgAB2PCYGE')

@bot.message_handler(commands=['start'])
def start_command(message):
  bot.send_message(message.chat.id, "Hello! Print /game for playing")

@bot.message_handler(commands=['stop'])
def start_command(message):
  chat_id = message.chat.id
  if database.isAlreadyStarted(chat_id) == 0:
    return
  database.stopped[chat_id] = 1
  bot.send_message(chat_id, "The game stopped!\nTo play again print /game")

@bot.message_handler(commands=['game'])
def game_command(message):
  chat_id = message.chat.id

  if database.isAlreadyStarted(chat_id):
    bot.send_message(chat_id, "The game already started. Print /stop to stop it")
    return
  genreButtons = controller.getGenreButtons()
  bot.send_message(chat_id, "Choose the genre of musics:", reply_markup = genreButtons)

@bot.message_handler(content_types=['text'])
def GetScore(message):
  chat_id = message.chat.id
  if database.isAlreadyStarted(chat_id) == 0:
    roundsButtons = controller.checkGenre(message, chat_id)
    if roundsButtons != 0:
      bot.send_message(chat_id, "Choose the genre of musics:", reply_markup = roundsButtons)
    else:
      round_number = controller.checkRounds(message)
      print(round_number)
      if round_number > 0:
          controller.startGame(bot, round_number, chat_id)
      else:
        bot.send_message(chat_id, "Wrong format")
  else:
      scoring.getScore(message.text, message.from_user.first_name, chat_id, bot)


bot.polling()
