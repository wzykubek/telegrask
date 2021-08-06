from telegram.ext import CallbackContext
from telegram import Update


class InlineQuery:
    def __init__(self, update: Update, context: CallbackContext) -> None:
        self.update = update
        self.context = context
        self.query_id = self.update.inline_query.id
        self.query_str = str(self.update.inline_query.query)
        self.query = self.query_str.split(" ")
        self.answers = []

    def add_answer(self, inline_query_result) -> None:
        self.answers.append(inline_query_result)

    def clear_answers(self) -> None:
        self.answers.clear()

    def send_answers(self) -> None:
        self.context.bot.answer_inline_query(self.query_id, self.answers, cache_time=0)
