#!/usr/bin/python3
"""Simple inline bot to send upper case, bold or italic text."""
# This program is dedicated to the public domain under the CC0 license.

from telegrask import Telegrask, InlineQuery
from telegram import InlineQueryResultArticle, InputTextMessageContent, ParseMode
from telegram.utils.helpers import escape_markdown
from uuid import uuid4

bot = Telegrask("BOT_TOKEN")
bot.config["HELP_MESSAGE"] = False


@bot.inline_query
def inline(query: InlineQuery):
    query_str = query.query_str
    if query_str == "":
        return

    query.add_answer(
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="Caps",
            input_message_content=InputTextMessageContent(query_str.upper()),
        )
    )
    query.add_answer(
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="Bold",
            input_message_content=InputTextMessageContent(
                f"*{escape_markdown(query_str)}*", parse_mode=ParseMode.MARKDOWN
            ),
        )
    )
    query.add_answer(
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="Italic",
            input_message_content=InputTextMessageContent(
                f"_{escape_markdown(query_str)}_", parse_mode=ParseMode.MARKDOWN
            ),
        )
    )

    query.send_answers()


if __name__ == "__main__":
    bot.run(debug=True)
