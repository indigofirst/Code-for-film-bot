import telebot
import random

# Инициализация бота с использованием его токена
bot = telebot.TeleBot("YOUR TOKEN")

# Списки фильмов
comedy_films = [
    "Superbad (2007)",
    "The Hangover (2009)",
    "Pineapple Express (2008)",
    "Step Brothers (2008)",
    "Anchorman (2004)"
]

horror_films = [
    "The Conjuring (2013)",
    "Hereditary (2018)",
    "It (2017)",
    "Get Out (2017)",
    "Paranormal Activity (2007)"
]

# Обработчик команды '/start', '/hello, /heh'
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот Который может посоветовать тебе фильмы! Вот команды - /filmcomedy - фильмы комедии. /filmhorror - фильмы хорроры.')

# Обработчик команды '/filmcomedy'
@bot.message_handler(commands=['filmcomedy'])
def send_comedy(message):
    film = random.choice(comedy_films)
    bot.reply_to(message, f"Как насчет этой комедии: {film}")

# Обработчик команды '/filmhorror'
@bot.message_handler(commands=['filmhorror'])
def send_horror(message):
    film = random.choice(horror_films)
    bot.reply_to(message, f"Как насчет этого хоррора: {film}")

# Запуск бота
bot.polling()
