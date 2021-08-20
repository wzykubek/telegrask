from telegram.ext import CallbackContext
from telegram import Update
from uuid import uuid4


class InlineQuery:
    """Class for inline query.

    Usage
    -----
        @bot.inline_query
        def inline(query: telegrask.InlineQuery):
            # update, context = query.update, query.context
            ...
    """

    def __init__(self, update: Update, context: CallbackContext) -> None:
        self.update = update
        self.context = context
        self.query_id = self.update.inline_query.id
        self.query_str = str(self.update.inline_query.query)
        self.query = self.query_str.split(" ")
        self.answers = []

    def add_answer(self, inline_query_result) -> None:
        """Add new answer to answers list.

        Usage
        -----
            answer = telegram.InlineQueryResultArticle(...)  # or other InlineQueryResult* type
            query.add_answer(answer)
            ...
            # after all you need to send all added results to user
            query.send_answers()
        """

        self.answers.append(inline_query_result)

    def clear_answers(self) -> None:
        """Clear all answers.

        Usage
        -----
            query.clear_answers()
        """

        self.answers.clear()

    def send_answers(self) -> None:
        """Send answers to user.

        Usage
        -----
            # execute at the end of callback function
            query.send_answers()
        """

        self.context.bot.answer_inline_query(self.query_id, self.answers, cache_time=0)

    def simple_return(self, inline_query_result) -> None:
        """Add and send to user only one result.

        Usage
        -----
            answer = telegram.InlineQueryResultArticle(...)  # or other InlineQueryResult* type
            query.simple_return(answer)
        """

        self.add_answer(inline_query_result)
        self.send_answers()

    @staticmethod
    def parse_description(desc: str) -> str:
        if len(desc) > 30:
            desc = str(desc[:32] + (desc[29:] and "..."))
        return desc

    @staticmethod
    def get_random_id() -> str:
        return str(uuid4())
