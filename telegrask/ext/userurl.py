from telegram import User


class UserURL:
    """Simle class to generate URL to user which can be sent in message.

    Usage
    -----
        ...
        # example
        user = update.message["reply_to_message"].from_user
        update.message.reply_text(
            f'User {UserURL(user)} has been muted.', 
            parse_mode="markdown"
        )
        ...
    """

    def __init__(self, user: User) -> None:
        self.user = user

    def __repr__(self) -> str:
        return f"[{self.user.first_name}](tg://user?id={self.user.id})"
