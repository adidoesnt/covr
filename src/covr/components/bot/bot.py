from telebot import TeleBot
from telebot.types import BotCommand
from typing import List
import threading

from covr.components.bot.constants import TELEGRAM_BOT_TOKEN
from covr.components.bot.config import config


bot = TeleBot(TELEGRAM_BOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help(message):
    response = config['responses']['start']['response']
    bot.reply_to(message, response)
    
@bot.message_handler(commands=['resume'])
def upload_resume(message):
    response = config['responses']['resume']['response']
    bot.reply_to(message, response)

def set_my_commands():
    try:
        commands: List[BotCommand] = []
        for command in config['commands']:
            commands.append(BotCommand(**command))
        
        bot.set_my_commands(commands)  
        print("Bot commands set successfully.")
    except Exception as e:
        print("Error setting commands:", e)
        exit(1)
        
def init_bot():
    set_my_commands()
    
    print("Starting bot...")
    bot.infinity_polling()
