import telebot
import bottokenforjust

bot = telebot.TeleBot(bottokenforjust.TOKEN)

@bot.message_handler(content_types=['text'])
def lalala(message):
    bot.send_message(message.chat.id, message.text)

bot.polling(non_stop=True)