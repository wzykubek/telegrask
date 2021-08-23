# Telegrask

![status](https://img.shields.io/pypi/status/telegrask?style=flat-square)
[![package version](https://img.shields.io/pypi/v/telegrask?style=flat-square)](https://pypi.org/project/Telegrask)
[![downloads](https://img.shields.io/pypi/dd/telegrask?style=flat-square)](https://pypi.org/project/Telegrask)
[![license](https://img.shields.io/github/license/samedamci/telegrask?style=flat-square)](https://github.com/samedamci/telegrask/blob/master/LICENSE)
[![docs](https://readthedocs.org/projects/telegrask/badge/?version=stable&style=flat-square)](https://telegrask.rtfd.io)
[![code style](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/psf/black)

---

Flask-inspired Telegram bot micro framework for Python.
Main idea is to use callback function decorators and make bot
creating more intuitive for developer.

## Installing

```shell
$ python3 -m pip install Telegrask
```

---

## Simple "Hello World" bot example

```python
from telegrask import Telegrask

bot = Telegrask("BOT_TOKEN")


@bot.command("hello", help='display "Hello, World!"')
def hello_command(update, context):
    update.message.reply_text("Hello, World!")


if __name__ == "__main__":
    bot.run(debug=True)
```

More examples in [examples](./examples) folder.

## Equivalent in pure [python-telegram-bot](https://python-telegram-bot.org/)

<details>
<summary>Click to show</summary>

```python
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
```

</details>

---

## Useful links

- [Documentation](http://telegrask.rtfd.io/)
- [PyPI Releases](https://pypi.org/project/Telegrask/)
