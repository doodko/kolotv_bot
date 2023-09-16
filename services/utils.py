from sqlalchemy import select

from database.db import Session
from database.models import Word


class Utils:
    def __init__(self, session: Session = Session()):
        self.session = session

    def make_pattern(self) -> str:
        with self.session.begin():
            all_patterns = self.session.execute(select(Word.pattern)).scalars().all()
            main_pattern = '|'.join(all_patterns)
            return main_pattern


    @staticmethod
    def get_full_chat_id(chat_id: int) -> int:
        return (chat_id + 1000000000000) * -1


utils = Utils()
      