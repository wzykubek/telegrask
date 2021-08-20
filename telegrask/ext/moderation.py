from telegram import Update, ChatPermissions
from telegram.ext import CallbackContext
from .chat import Chat
from typing import Optional, Union
from datetime import datetime


class Moderation(Chat):
    """Class with methods useful for moderating.

    Usage
    -----
        mod = Moderation(update, context)

        # Simple way to get user ID from message you replied with command.
        user_id = update.message["reply_to_message"].from_user.id
        ...
    """

    def __init__(self, update: Update, context: CallbackContext) -> None:
        self.update = update
        self.context = context
        super().__init__(update, context)

    def change_permissions(
        self,
        user_id: int,
        until_date: Union[int, datetime] = None,
        permissions: ChatPermissions = None,
    ) -> None:
        """Change any permission to user in chat."""

        if not self.is_user_admin(user_id):
            self.context.bot.restrict_chat_member(
                self.chat_id, user_id, permissions=permissions, until_date=until_date,
            )
        else:
            raise PermissionError("Cannot change chat admin permissions")

    def mute(self, user_id: int, until_date: Union[int, datetime] = None) -> None:
        """Mute user in chat."""

        perms = ChatPermissions(can_send_messages=False)
        self.change_permissions(user_id, until_date, perms)

    def unmute(self, user_id: int) -> None:
        """Restore permissions to restricted (or muted) user."""

        perms = ChatPermissions(
            can_send_messages=False,
            can_send_media_messages=True,
            can_send_polls=True,
            can_send_other_messages=True,
            can_add_web_page_previews=True,
        )
        self.change_permissions(user_id, permissions=perms)

    def ban(
        self,
        user_id: int,
        until_date: Union[int, datetime] = None,
        revoke_messages: bool = False,
    ) -> None:
        """Ban user in chat."""

        if not self.is_user_admin(user_id):
            self.context.bot.ban_chat_member(
                self.chat_id,
                user_id,
                until_date=until_date,
                revoke_messages=revoke_messages,
            )
        else:
            raise PermissionError("Cannot ban chat admin")

    def unban(self, user_id: int) -> None:
        """Unban banned user in chat."""

        if not self.is_user_admin(user_id):
            self.context.bot.unban_chat_member(self.chat_id, user_id)
        else:
            raise PermissionError("Cannot unban chat admin")
