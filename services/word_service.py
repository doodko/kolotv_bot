from database.db import Session
from database.models import Word


class WordService:
    def __init__(self, session: Session = Session()):
        self.session = session

    def add_new_word(self, name: str, pattern: str):
        new_word = Word(name=name, pattern=pattern)
        self.session.add(new_word)
        self.session.commit()

    def get_all_words(self):
        return self.session.query(Word).all()

    def seed_db(self):
        words_list = [('коло', '\\bколо\\b'),
                      ('провайдер', '\\bпровайдер'),
                      ('інтернет', '\\b[іи]нтернет'),
                      ('локалнет', '\\bлокалн[еэє]т\\b'),
                      ('павутина', '\\bпав?утин'),
                      ('wi-fi', '\\b(wi\\-?fi|вай\\-?фай)\\b'),
                      ('утелс', '\\b(utels|утелс)\\b'),
                      ('вега', '\\b(vega|вега)\\b'),
                      ('київстар', '\\b(ки[їєе]встар|kyivstar)'),
                      ('роутер', '\\bроутер')]

        for word in words_list:
            name, pattern = word
            self.add_new_word(name=name, pattern=pattern)
