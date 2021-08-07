from telegram.ext import Updater, CommandHandler, InlineQueryHandler, CallbackContext
from telegram import ParseMode, Update
from .exceptions import InvalidBotToken, HelpPrasingError
from .helpparser import HelpParser
from typing import Union, Callable, Optional


class Telegrask:
    """Main bot class"""

    def __init__(self, token: str, help_message: bool = True) -> None:
        if not token:
            raise InvalidBotToken("Token not specified")
        self.config = {"token": token, "help_message": help_message}
        self.updater = Updater(self.config["token"], use_context=True)
        self.dispatcher = self.updater.dispatcher
        self.help = HelpParser()

    def command(self, commands: Union[str, list], description: Optional[str] = None) -> Callable:
        """Decorate command callback function. Add CommandHandler to dispatcher
        and command description for HelpParser.
        """

        def w(f):
            self.dispatcher.add_handler(CommandHandler(commands, f))
            command_name = commands[0] if type(commands) == list else commands
            if self.config["help_message"]:
                if description is None:
                    raise HelpPrasingError("Description for command is not provided")
                self.help.add_command(command_name, description)

        return w

    def inline_query(self, f: Callable) -> None:
        self.dispatcher.add_handler(InlineQueryHandler(f))

    def __help_command(self, update: Update, context: CallbackContext) -> None:
        update.message.reply_text(self.help.content, parse_mode=ParseMode.MARKDOWN)

    def run(self, debug: bool = False) -> None:
        if self.config["help_message"]:
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
