from dotenv import load_dotenv; load_dotenv()
import telebot
from telebot import types
from api import AI_Api
from os import getenv


IKM = types.InlineKeyboardMarkup
IKB = types.InlineKeyboardButton
MSG = types.Message


bot = telebot.TeleBot(getenv("TOKEN"))
api = AI_Api("Ты - студентка Катя, которая учится в ГУАП в Санкт-Перербурге и рассказывает короткие истории из студенческой жизни. Анализируешь информацию из файла и с сайта ГУАП  https://guap.ru/ и https://priem.guap.ru/ ", 64)


@bot.callback_query_handler(func=lambda callback: True)
def callback(callback) -> None:
    if callback.data == 'talk':
        bot.send_message(callback.message.chat.id, f"Привет! Конечно, давай поговорим. Что тебя интересует из студенческой жизни?")
    if callback.data == 'links':
        bot.send_message(callback.message.chat.id, f"Официальный сайт для поступающих - https://priem.guap.ru/ \n\nОфициальная тг группа - https://t.me/new_guap\n\nОфициальная вк группа - https://t.me/new_guap\n\nОфициальный сайт ВУЗа - https://guap.ru/")


@bot.message_handler(commands=['start'])
def start(msg: MSG) -> None:
    buttons = [
        IKB(text="Поговорить с Катей", callback_data='talk'),
        IKB(text="Путеводитель по чатам и пабликам ГУАП", callback_data='links')
    ]
    markup = IKM()
    for btn in buttons:
        markup.add(btn)
    bot.send_message(msg.chat.id,f"{msg.from_user.first_name}, привет! Я Катя из гуапа, твой личный помощник в поступлении. \n\n\nТы можешь меня спросить о чем угодно, вот тебе наводящие темы:\n\n\n▫️почему стоит поступать именно в гуап?\n▫️можешь узнать все направления подготовки\n▫️расспросить подробно про любое направление\n\n\nТак же, ты можешь просто пообщаться со мной и спрашивать вопросы не только про вуз",reply_markup=markup)


@bot.message_handler(content_types=['text'])
@bot.message_handler(commands=['talk'])
def get_text(msg: MSG) -> None:
    answer = api.search(msg.text)
    bot.send_message(msg.from_user.id, answer)


@bot.message_handler(commands=['links'])
def links(message) -> None:
    bot.send_message(message.from_user.id,f"Официальный сайт для поступающих - https://priem.guap.ru/ \n\nОфициальная тг группа - https://t.me/new_guap\n\nОфициальная вк группа - https://t.me/new_guap\n\nОфициальный сайт ВУЗа - https://guap.ru/")