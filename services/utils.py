from sqlalchemy import select, func

from database.db import Session
from database.models import Word, Mention


class Utils:
    def __init__(self, session: Session = Session()):
        self.session = session

    def make_pattern(self):
        with self.session.begin():
            all_patterns = self.session.execute(select(Word.pattern)).scalars().all()
            main_pattern = '|'.join(all_patterns)
            return main_pattern

    def give_statistics(self):
        chats_count = self.session.query(Mention.chat_id).distinct().count()
        words_counts = self.count_mentions()
        msg = f"За останні 30 днів пошукові слова зустрічались у <b>{chats_count}</b> чатах.\n\n" \
              f"Найчастіше згадують:\n{words_counts}"

        return msg

    def count_mentions(self) -> str:
        words_counts = self.session.query(Word.name, func.count(Mention.id)).join(Word.mentions).group_by(
            Word.name).order_by(func.count(Mention.id).desc()).all()
        words_string = '\n'.join([f"{word}: {count}" for word, count in words_counts])
        return words_string

utils = Utils()
      