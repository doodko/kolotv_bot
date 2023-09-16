from database.db import Session
from database.models import Word


class WordService:
    def __init__(self, session: Session = Session()):
        self.session = session

    def add_new_word(self, name: str, pattern: str):
        new_word = Word(name=name, pattern=pattern)
        self.session.add(new_word)
        self.session.commit()

    def get_all_words(self) -> list[Word]:
        return self.session.query(Word).all()



word_service = WordService()

