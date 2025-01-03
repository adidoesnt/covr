from telebot import TeleBot
from telebot.types import BotCommand, Message
from typing import List

from covr.components.bot.constants import TELEGRAM_BOT_TOKEN
from covr.components.bot.config import config
from covr.components.resume.parser import parse_pdf
from covr.components.resume.uploader import check_if_resume_exists, upload_resume as save_resume_to_db, delete_resume
from covr.components.langchain.vector_store import query_user_collection

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
    
    is_resume_uploaded = check_if_resume_exists(user_id=user_id)
    
    if is_resume_uploaded:
        delete_resume(user_id=user_id)
    
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
    
@bot.message_handler(commands=['query'])
def handle_query_request(message):
    user = message.from_user
    user_id = user.id
    
    is_resume_uploaded = check_if_resume_exists(user_id=user_id)
    
    if not is_resume_uploaded:
        response = config['responses']['no_resume']['response']
        bot.reply_to(message, response)
        return
    
    response = config['responses']['query_prompt']['response']
    bot.reply_to(message, response)
    
    bot.register_next_step_handler(callback=handle_query, message=message)
    
def handle_query(message: Message):
    user = message.from_user
    user_id = user.id
    
    query = message.text
    bot.reply_to(message=message, text=config['responses']['querying_resume']['response'])
    
    try:
        response = query_user_collection(user_id=user_id, query=query)
        bot.reply_to(message=message, text=response)
    except Exception as e:
        print(e)
        response = config['responses']['query_error']['response']
        bot.reply_to(message=message, text=response)
    
@bot.message_handler(commands=['coverletter'])
def handle_coverletter_request(message):
    user = message.from_user
    user_id = user.id
    
    is_resume_uploaded = check_if_resume_exists(user_id=user_id)
    
    if not is_resume_uploaded:
        response = config['responses']['no_resume']['response']
        bot.reply_to(message, response)
        return
    
    response = config['responses']['coverletter']['response']
    bot.reply_to(message, response)
    
    bot.register_next_step_handler(callback=generate_cover_letter, message=message)
    
def generate_cover_letter(message: Message):
    bot.reply_to(message=message, text=config['responses']['coverletter_generating']['response'])
    
    user = message.from_user
    user_id = user.id
    
    message_text = message.text
    
    # cover_letter = generate_cover_letter_response(user_id=user_id, job_description=message_text)
    response = config['responses']['coverletter_generated']['response']
    # TODO: response += f"\n\n{cover_letter}"

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
