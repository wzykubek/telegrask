from telegram import Update
from telegram.ext import CallbackContext
from . import bot


@bot.command("hello", help='reply "Hello, World!" text')
def hello(update: Update, context: CallbackContext):
    update.message.reply_text("Hello, World!")
