import telebot, requests
from loguru import logger
# from flask import Flask, request
from config import TOKEN, URL_PING
from func import ping_pong,approve


logger.add("debug.log", level="DEBUG", format="{time} {level} {message}")
bot = telebot.TeleBot(TOKEN)



@bot.message_handler(commands=['start'])
@logger.catch
def send_welcome(message):
    bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}')

@bot.message_handler(commands=['ping'])
@logger.catch
def send_ping(message):
    try:
        response = ping_pong()
    except:
        bot.send_message(message.chat.id, "Сервер не доступен")
    bot.send_message(message.chat.id, f'Результат запроса: {response["result"]}')


@bot.message_handler(commands=['approve'])
@logger.catch
def send_approve(message):
    try:
        response = approve()
    except:
        bot.send_message(message.chat.id, "Сервер не доступен")
    bot.send_message(message.chat.id, f'Результат запроса: {response["result"]}')


if __name__ == "__main__":
    bot.infinity_polling()