class HelpParser:
    """Parser of help message often sended by /help or /start command."""

    def __init__(self) -> None:
        self.header = "Available commands"
        self.commands_descriptions = dict()

    def add_command(self, name: str, help: str) -> None:
        self.commands_descriptions[name] = help

    @property
    def content(self) -> str:
        final_message = f"*{self.header}*\n\n"
        for cmd, desc in self.commands_descriptions.items():
            final_message += f"/{cmd}\n{desc}\n\n"
        return final_message
