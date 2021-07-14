import telebot
import randomMusic

bot = telebot.TeleBot('1847617795:AAGC9PPTMvbl9FeoGG2-4gcywEgAB2PCYGE');

@bot.message_handler(commands=['start'])
def start_command(message):
	bot.send_message(message.chat.id, "Hello daun! Print /game for playing")
@bot.message_handler(commands=['game'])
def game_command(message):
	bot.send_message(message.chat.id, "Processing music...")
	print(randomMusic.Get());
	bot.send_audio(message.chat.id, randomMusic.Get())

bot.polling()