Usage Basics
============

Main goal of this framework is use handlers decorators and make bot creating more intuitive.

Simplest Example
----------------

Hello World bot example in Telegrask:

.. code-block:: python

    from telegrask import Telegrask

    bot = Telegrask("TOKEN")


    @bot.command("hello", help='display "Hello, World!"')
    def hello_command(update, context):
        update.message.reply_text("Hello, World!")


    if __name__ == "__main__":
        bot.run(debug=True)

and equivalent code in pure `python-telegram-bot <https://github.com/python-telegram-bot/python-telegram-bot>`_ library:

.. code-block:: python

    from telegram.ext import Updater, CommandHandler
    from telegram import ParseMode
    import logging

    logging.basicConfig(format="%(levelname)s - %(message)s", level=logging.DEBUG)
    logger = logging.getLogger(__name__)


    def hello_command(update, context):
        update.message.reply_text("Hello, World!")


    def help_command(update, context):
        help_content = """*Available commands*

    /hello
    display "Hello, World!"

    /help
    display this message
    """
        update.message.reply_text(help_content, parse_mode=ParseMode.MARKDOWN)


    def main():
        global updater
        updater = Updater("BOT_TOKEN")
        dispatcher = updater.dispatcher
        dispatcher.add_handler(CommandHandler("hello", hello_command))
        dispatcher.add_handler(CommandHandler(["help", "start"], help_command))
        updater.start_polling()
        updater.idle()


    if __name__ == "__main__":
        main()