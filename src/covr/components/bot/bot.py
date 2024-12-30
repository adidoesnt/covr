from telebot import TeleBot
from telebot.types import BotCommand, Message
from typing import List

from covr.components.bot.constants import TELEGRAM_BOT_TOKEN
from covr.components.bot.config import config
from covr.components.resume_parser.parser import parse_pdf
from covr.components.chromadb.db import upload_resume as save_resume_to_db, check_if_resume_exists


bot = TeleBot(TELEGRAM_BOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help(message: Message):
    response = config['responses']['start']['response']
    bot.reply_to(message, response)
    
@bot.message_handler(commands=['resume'])
def upload_resume(message: Message):
    user = message.from_user
    user_id = user.id
    
    is_resume_uploaded = check_if_resume_exists(user_id=user_id)
    
    if is_resume_uploaded:
        response = config['responses']['file_uploaded']['response']
        bot.reply_to(message, response)
        return
    
    response = config['responses']['resume']['response']
    bot.reply_to(message, response)
    
@bot.message_handler(content_types=['document'])
def file_handler(message: Message):
    user = message.from_user
    user_id = user.id
    
    file_id = message.document.file_id
    file = bot.get_file(file_id=file_id)
    
    if not file.file_path.endswith('.pdf'):
        response = config['responses']['invalid_file']['response']
        bot.reply_to(message, response)
        return
    
    file = bot.download_file(file_path=file.file_path)
    parsed_file_content = parse_pdf(file_content=file)
    
    save_resume_to_db(user_id=user_id, file_content=parsed_file_content)
    response = config['responses']['file_uploaded']['response']
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
