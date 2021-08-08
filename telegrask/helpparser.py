class HelpParser:
    """Parser of help message often sended by /help or /start command."""

    def __init__(self, inline: bool = False) -> None:
        self.__message = "*Available commands*\n\n"
        self.__final_message = self.__message
        self.commands_descriptions = dict()

    def add_command(self, name: str, help: str) -> None:
        self.commands_descriptions[name] = help

    @property
    def content(self) -> str:
        for cmd, desc in self.commands_descriptions.items():
            self.__final_message += f"/{cmd}\n{desc}\n\n"
        return self.__final_message
