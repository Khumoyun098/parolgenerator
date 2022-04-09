import os
from main import gen_pass
import telebot
from telebot.types import BotCommand

# get token from env

token = os.environ.get('TOKEN')

bot = telebot.TeleBot(token=token, parse_mode='html')

BOT_COMMANDS = [
    {
        "command": 'start',
        "description": "Start"
    },
    {
        "command": 'generate',
        "description": "Parol generatsiya qilish"
    },
]

bot.set_my_commands(
    commands=[BotCommand(command['command'], command['description']) for command in BOT_COMMANDS]
)


@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Men parol generatsiya qilaman. /generate ni jo'nating")

@bot.message_handler(commands=['generate'])
def generate_password(message):
    pswd = gen_pass()
    pswd = "\n".join(pswd)
    bot.reply_to(message, f"<code>{pswd}</code>")



bot.infinity_polling()