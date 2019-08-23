import telebot

api_key = "960836909:AAGTzXy9BPp-xwMBUNI3PIr11PragYf9phY"
bot = telebot.TeleBot(api_key)


@bot.message_handler(commands=['start'])
def start_message(message):
    print(message)
    bot.send_message(message.chat.id, 'Привет, ты написал мне')


bot.polling()
