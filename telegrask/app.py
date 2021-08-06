from telegram.ext import Updater, CommandHandler, InlineQueryHandler, CallbackContext
from telegram import ParseMode, Update
from .exceptions import InvalidBotToken
from .helpparser import HelpParser
from typing import Union, Callable


class Telegrask:
    """Main bot class"""

    def __init__(self, token: str) -> None:
        if not token:
            raise InvalidBotToken("Token not specified")
        self.updater = Updater(token, use_context=True)
        self.dispatcher = self.updater.dispatcher
        self.help = HelpParser()

    def command(self, commands: Union[str, list], description: str) -> Callable:
        """Decorate command callback function. Add CommandHandler to dispatcher
        and command description for HelpParser.
        """

        def w(f):
            self.dispatcher.add_handler(CommandHandler(commands, f))
            command_name = commands[0] if type(commands) == list else commands
            self.help.add_command(command_name, description)

        return w

    def inline_query(self, f: Callable) -> None:
        self.dispatcher.add_handler(InlineQueryHandler(f))

    def __help_command(self, update: Update, context: CallbackContext) -> None:
        update.message.reply_text(self.help.content, parse_mode=ParseMode.MARKDOWN)

    def run(self, debug: bool = False) -> None:
        self.command(["help", "start"], description="display this message")(
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
