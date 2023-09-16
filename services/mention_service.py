import re
from datetime import datetime

from aiogram.types import Message
from sqlalchemy import func

from database.db import Session
from database.models import Mention, Word
from services.utils import utils
from services.word_service import word_service


class MentionService:
    def __init__(self, session: Session = Session()):
        self.session = session

    @staticmethod
    def get_mentions_list(message: Message) -> list[Word]:
        return [word for word in word_service.get_all_words() if re.search(word.pattern, message.text.lower())]

    def add_mentions(self, words: list[Word], message: Message) -> None:
        chat = utils.get_full_chat_id(chat_id=message.chat.id)
        link = f"https://t.me/c/{chat}/{message.message_id}"

        mentions = [Mention(date=datetime.now(), word_id=word.id,chat_id=message.chat.id, link=link) for word in words]

        self.session.add_all(mentions)
        self.session.commit()

    def give_statistics(self) -> str:
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



mention_service = MentionService()
