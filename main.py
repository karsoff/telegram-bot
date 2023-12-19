import telebot
import datetime
from cfg import *
import requests
import json
from telebot import types

bot = telebot.TeleBot(TOKEN)
API='959a554bf3cf48813002245922518c6b'


@bot.message_handler(commands=["start"])

def start(message):

    mess=f"Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b>"
    bot.send_message(message.chat.id, mess, parse_mode="html")


@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id,"На данный момент бот знает эти команды:", parse_mode="html")
    bot.send_message(message.chat.id, "/list - просмотр расписания на сегодня и всю неделю", parse_mode="html")
    bot.send_message(message.chat.id, "/weather - показывает погоду в Перми", parse_mode="html")
    bot.send_message(message.chat.id,"/help - помощь", parse_mode="html")



@bot.message_handler(commands=["list"])
def list(message):
    time=datetime.datetime.now()
    bot.send_message(message.chat.id,time)
    if(time.day==19):
        bot.send_message(message.chat.id,
                         "1 пара(8:00) Введение в операционные системы и инструменты разработки (практ) ауд. 520/2",
                         parse_mode="html")
        bot.send_message(message.chat.id, "2 пара(9:45) Введение в алгоритмы и структуры данных (лек) ауд. 512/2",
                         parse_mode="html")
        bot.send_message(message.chat.id, "3 пара(11:30) Языки программирования I (практ) ауд. 522/2",
                         parse_mode="html")
        if(time.day==20):
            bot.send_message(message.chat.id,"Пар нет",parse_mode="html")
        if(time.day==21):
            bot.send_message(message.chat.id,"1 пара(8:00) Линейная алгебра (лек) ауд. 202/8")
            bot.send_message(message.chat.id, "3 пара(11:30) Основы российской государственности (практ) ауд. 221/11")
        if(time.day==22):
            bot.send_message(message.chat.id,"1 пара(8:00) Введение в алгоритмы и структуры данных (практ) ауд. 424/8")
            bot.send_message(message.chat.id,"2 пара(9:45) Линейная алгебра (практ) ауд. 326/12")
        if(time.day==23):
            bot.send_message(message.chat.id,"2 пара(9:45) Введение в математический анализ (лек) ауд. 202/8")




    #file = open('./photo.jpg','rb')
    #bot.send_photo(message.chat.id,file)

@bot.message_handler(commands=['weather'])
def weather(message):
    res = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Perm&appid=959a554bf3cf48813002245922518c6b&units=metric')
    data = json.loads(res.text)
    bot.reply_to(message, f"сейчас погода: {data['main']['temp']}")



bot.polling(none_stop=True)
