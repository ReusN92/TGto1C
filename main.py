import telebot
from loguru import logger
# from flask import Flask, request
from config import TOKEN

logger.add("debug.log", level="DEBUG", format="{time} {level} {message}")
bot = telebot.TeleBot(TOKEN)



@bot.message_handler(commands=['start'])
@logger.catch
def send_welcome(message):
    bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}')
    logger.critical('msg sended')


if __name__ == "__main__":
    bot.infinity_polling()