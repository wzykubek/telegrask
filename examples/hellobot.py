#!/usr/bin/python3
"""Simplest bot which reply "Hello, World!" string."""
# This program is dedicated to the public domain under the CC0 license.

from telegrask import Telegrask

bot = Telegrask("BOT_TOKEN")


@bot.command("hello", help='display "Hello, World!"')
def hello_command(update, context):
    update.message.reply_text("Hello, World!")


if __name__ == "__main__":
    bot.run(debug=True)
