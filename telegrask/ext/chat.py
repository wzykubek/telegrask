from telegram import Update
from telegram.ext import CallbackContext


class Chat:
    """Class to get basic info about chat in unified object.

    Usage
    -----
        chat = Chat(update, context)
    """

    def __init__(self, update: Update, context: CallbackContext) -> None:
        self.update = update
        self.context = context

        self.chat_id = self.update.message.chat.id

    @property
    def admins(self) -> list:
        admins = self.context.bot.get_chat_administrators(self.chat_id)
        return admins

    @property
    def admins_ids(self) -> list:
        return [admin.user.id for admin in self.admins]

    @property
    def admins_usernames(self) -> list:
        return [admin.user.username for admin in self.admins]

    def is_user_admin(self, user_id: int) -> bool:
        return user_id in self.admins_ids
