# импорт библиотеки телебот
import os
import telebot
import random

# Токен твоего бота, полученный от BotFather в Telegram
TOKEN = '8544193969:AAE70uodbN_N549epKi5_DDXYD8lCvDNIro'

# Создаем экземпляр бота
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['photo'])
def send_photo(message):
    chat_id = message.chat.id
    if photo_directory:
        file_path = random.choice(photo_directory)
        with open(file_path, 'rb') as photo_file:
            bot.send_photo(chat_id, photo_file)
    else:
        bot.send_message(chat_id, 'В данной директории нет файлов.')

@bot.message_handler(commands=['add_meme'])
def add_photo(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Отправьте свой мем.")





photo_directory = ['photo/cat.png', 'photo/ff9a0ae6fbadcb9752710613a6e99f75.jpg', 'photo/mem.png']





# Запускаем бота
bot.polling()
