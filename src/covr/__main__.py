from threading import Thread, Event

from covr.components.bot.bot import init_bot

shutdown_event = Event()
bot_thread = Thread(target=init_bot, daemon=True)

bot_thread.start()

try:
    bot_thread.join()
except KeyboardInterrupt:
    print("Shutting down...")
    shutdown_event.set()
