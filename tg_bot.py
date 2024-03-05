from dotenv import load_dotenv
import telebot
import re
from telebot.types import Message
from api import AI_Api
from os import getenv


load_dotenv()
bot = telebot.TeleBot(getenv("TOKEN"))
api = AI_Api("Ты - студентка Катя, которая учится в ГУАП в Санкт-Перербурге и рассказывает истории из студенческой жизни", 64)

# Функция для подсчёта слов
def count(text: str) -> int:
    return len(re.findall(r"\w+", text))


@bot.message_handler(commands=['start'])
def start(msg: Message):
    print("Called Start")
    bot.send_message(msg.from_user.id, "Привет! Задай свой вопрос!")

@bot.message_handler(content_types=['text'])
def get_text(msg: Message):
    print(f"Called Query by {msg.from_user.first_name}")
    answer = api.search(msg.text)
    bot.send_message(msg.from_user.id, answer)

