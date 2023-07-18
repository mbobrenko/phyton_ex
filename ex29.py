import telebot
from random import *
import json
from telebot import types
films=[]


def save():
    with open("films.json","w",encoding="utf-8") as fh:
        fh.write(json.dumps(films,ensure_ascii=False))
    print("У нас отлично получилось сохранить фильмы films.json")

def load():
    global films
    with open("films.json","r",encoding="utf-8") as fh:
        films=json.load(fh)
    print("фильмотека была успешна загружена°")   


API_TOKEN='..........BOTFATHER'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    try:
        load()
        bot.send_message(message.chat.id,"загружено°!")

    except:
        films.append("ккк°")
        films.append("ннн")
        films.append("ффф пуфик")
        films.append("mmm")
        films.append("пан°") 
        bot.send_message(message.chat.id,"фильмотека была загружена по умолчанию")


@bot.message_handler(commands=['all'])
def show_all(message):
    bot.send_message(message.chat.id,"вот список фильмов")
    bot.send_message(message.chat.id, ", ".join(films))

@bot.message_handler(content_types='text')
def message_reply(message):
    if 'привет‚' in message.text :
        bot.send_message(message.chat.id,'и тебе привет')
    else: 
	    bot.send_message(message.chat.id,'Моя твоя не понимат')
bot.polling()

