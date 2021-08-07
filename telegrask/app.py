from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    InlineQueryHandler,
    CallbackContext,
)
from telegram import ParseMode, Update
from telegram.ext.filters import Filters
from .exceptions import HelpPrasingError
from .helpparser import HelpParser
from .config import Config
from typing import Union, Callable, Optional, Pattern


class Telegrask:
    """Main bot class.

    Usage
    -----
        bot = Telegrask(TOKEN)

        # optional configuration
        bot.config["ATTRIBUTE_NAME"] = attribute_value
    """

    default_config = Config({"HELP_MESSAGE": True})

    def __init__(self, token: str) -> None:
        self.config = self.default_config
        self.updater = Updater(token, use_context=True)
        self.dispatcher = self.updater.dispatcher
        self.help = HelpParser()

    def command(
        self, commands: Union[str, list], help: Optional[str] = None
    ) -> Callable:
        """Decorator for command callback function.

        Usage
        -----
            @bot.command("command_name", help="command help message")
            def callback_function(update, context):
                ...
        """

        def w(f):
            self.dispatcher.add_handler(CommandHandler(commands, f))
            command_name = commands[0] if type(commands) == list else commands
            if self.config["HELP_MESSAGE"]:
                if help is None:
                    raise HelpPrasingError("Help for command is not provided")
                self.help.add_command(command_name, help)

        return w

    def message(self, filters: Filters) -> Callable:
        """Decorator for message callback function based on filters.

        Usage
        -----
            @bot.message(telegram.ext.filters.Filters.*)
            def callback_function(update, context):
                ...
        """

        return lambda f: self.dispatcher.add_handler(MessageHandler(filters, f))

    def message_regex(self, regex: Pattern) -> Callable:
        """Wrapper decorator for `self.message` used for handle messages
        by regexes.

        Usage
        -----
            @bot.message_regex("text or regex")
            def callback_function(update, context):
                ...
        """

        return lambda f: self.message(Filters.regex(regex))(f)

    def inline_query(self, f: Callable) -> None:
        """Decorator for inline query callback function.

        Usage
        -----
            @bot.inline_query
            def callback_function(update, context):
                ...
        """

        self.dispatcher.add_handler(InlineQueryHandler(f))

    def __help_command(self, update: Update, context: CallbackContext) -> None:
        """Send help message with description of each command."""

        update.message.reply_text(self.help.content, parse_mode=ParseMode.MARKDOWN)

    def run(self, debug: bool = False) -> None:
        """Start bot.

        Usage
        -----
            # execute at the end
            bot.run(debug=True)
        """

        if self.config["HELP_MESSAGE"]:
            self.command(["help", "start"], help="display this message")(
                self.__help_command
            )

        if debug:
            import logging

            logging.basicConfig(
                format="%(levelname)s - %(message)s", level=logging.DEBUG
            )
            logger = logging.getLogger(__name__)

        self.updater.start_polling()
        self.updater.idle()
