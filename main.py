import telebot, requests
from loguru import logger
# from flask import Flask, request
from config import TOKEN, URL_PING, URL_APPROVE
from func import req


logger.add("debug.log", level="DEBUG", format="{time} {level} {message}")
bot = telebot.TeleBot(TOKEN)



@bot.message_handler(commands=['start'])
@logger.catch
def send_welcome(message):
    bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}')

@bot.message_handler(commands=['ping'])
@logger.catch
def send_ping(message):
    response = req(URL_PING)
    bot.send_message(message.chat.id, f'Результат запроса: {response["result"]}')


@bot.message_handler(commands=['approve'])
@logger.catch
def send_approve(message):
    response = req(URL_APPROVE)
    bot.send_message(message.chat.id, f'Результат запроса: {response["result"]}')


if __name__ == "__main__":
    bot.infinity_polling()