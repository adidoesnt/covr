from threading import Thread, Event
import time

from covr.components.bot.bot import init_bot
from covr.components.resume_parser.queue import pull_messages
from covr.components.chromadb.db import connect_chromadb

shutdown_event = Event()

connect_chromadb()

bot_thread = Thread(target=init_bot, daemon=True)
resume_queue_thread = Thread(target=pull_messages, daemon=True)

bot_thread.start()

time.sleep(1)
resume_queue_thread.start()

try:
    bot_thread.join()
    resume_queue_thread.join()
except KeyboardInterrupt:
    print("Shutting down...")
    shutdown_event.set()
