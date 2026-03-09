# импорт библиотеки телебот
import os
import telebot
import random

# Токен твоего бота, полученный от BotFather в Telegram
TOKEN = '8544193969:AAE70uodbN_N549epKi5_DDXYD8lCvDNIro'

# Создаем экземпляр бота
bot = telebot.TeleBot(TOKEN)
facts = [
    'Осьминоги имеют три сердца.',
    'Мёд никогда не портится — его находили в египетских пирамидах.',
    'Бананы слегка радиоактивны.',
    'Улитки могут спать до 3 лет.',
    'Молния бьёт в Землю около 100 раз в секунду.',
]

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет!\nНапиши /random_fact чтобы узнать интересный факт.\n/add_meme чтобы добавить мем'
                                      '\n/meme чтобы посмотреть случайный мем'
                                      '\nПриятного пользования!')

@bot.message_handler(commands=['random_fact'])
def random_fact(message):
    fact = random.choice(facts)
    bot.send_message(message.chat.id, fact)

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
