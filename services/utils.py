from datetime import timedelta, datetime

from sqlalchemy import select

from database.db import Session
from database.models import Word


class Utils:
    @staticmethod
    def make_pattern() -> str:
        with Session() as session:
            all_patterns = session.execute(select(Word.pattern)).scalars().all()
            main_pattern = '|'.join(all_patterns)
            return main_pattern

    @staticmethod
    def get_full_chat_id(chat_id: int) -> int:
        return (chat_id + 1000000000000) * -1

    @staticmethod
    def get_month_string(number: int) -> str:
        if number % 10 == 1 and number % 100 != 11:
            return f"{number} місяць"
        elif 2 <= number % 10 <= 4 and (number % 100 < 10 or number % 100 >= 20):
            return f"{number} місяці"
        else:
            return f"{number} місяців"

    @staticmethod
    def months_ago(months: int) -> datetime:
        today = datetime.now()
        days_ago = 365 // 12 * months
        return today - timedelta(days=days_ago)


utils = Utils()
