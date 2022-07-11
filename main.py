import telebot, requests
from loguru import logger
from flask import Flask, request, jsonify, json
from config import TOKEN, URL_PING, URL_APPROVE
from func import req, FuncDB

app = Flask(__name__)

logger.add("debug.log", level="DEBUG", format="{time} {level} {message}")
bot = telebot.TeleBot(TOKEN)
bot.send
@logger.catch
@app.route('/json-example',methods=['POST'])
def json_example():
    request_data = request.get_json()

    number = request_data['number']
    message = request_data['message']
    file = request_data['files']
    buttons = request_data['buttons']
    id = request_data['id']
    send_to = request_data['send_to']
    logger.info(message)
    FuncDB.add_new_notifi(number=number, message=message, file=file, buttons=buttons, id=id, send_to=send_to, status='new')

    data = {"status":"Verified"}
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

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

@app.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@app.route('/', methods=["GET"])
def index():
    return "Hello from Ngrok!", 200

if __name__ == "__main__":
    bot.set_webhook(url='https://808f-91-235-224-89.eu.ngrok.io/' + TOKEN)
    print(bot.get_webhook_info().__dict__)
    #server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
    app.run(debug=True, port=5000)