# импорт библиотеки телебот
import os
import telebot
import random

# Токен твоего бота, полученный от BotFather в Telegram
TOKEN = '8544193969:AAE70uodbN_N549epKi5_DDXYD8lCvDNIro'

# Создаем экземпляр бота
bot = telebot.TeleBot(TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
   text = 'Hello'
   # Отправляем сообщение text пользователю
   bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['photo'])
def send_photo(message):
    chat_id = message.chat.id
    files = os.listdir(photo_directory)
    if files:
        random_file = random.choice(files)
        file_path = os.path.join(photo_directory, random_file)
        print(file_path)
        with open(file_path, 'rb') as photo_file:
            bot.send_photo(chat_id, photo_file)
    else:
        bot.send_message(chat_id, 'В данной директории нет файлов.')

photo_directory = r"C:\Users\user\Desktop\dads"



# Запускаем бота
bot.polling()
