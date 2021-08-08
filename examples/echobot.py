#!/usr/bin/python3
"""Simple bot to reply exactly the same what user sent to chat."""
# This program is dedicated to the public domain under the CC0 license.

from telegrask import Telegrask

bot = Telegrask("BOT_TOKEN")


@bot.command("echo", help="repeat user words", allow_without_prefix=True)
def echo(update, context):
    update.message.reply_text(update.message.text)


if __name__ == "__main__":
    bot.run(debug=True)
