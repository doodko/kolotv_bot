import re
from datetime import datetime

from aiogram.types import Message

from database.db import Session
from database.models import Mention
from services.word_service import word_service


class MentionService:
    def __init__(self, session: Session = Session()):
        self.session = session

    def add_new_mention(self, message: Message) -> None:
        for word in word_service.get_all_words():
            if re.search(word.pattern, message.text.lower()):
                new_mention = Mention(date=datetime.now(),
                                      word_id=word.id,
                                      chat_id=message.chat.id,
                                      link=self.make_msg_link(message=message))
                self.session.add(new_mention)
                self.session.commit()

    @staticmethod
    def make_msg_link(message: Message) -> str:
        chat_id = (message.chat.id + 1000000000000) * -1
        message_id = message.message_id
        link = f"https://t.me/c/{chat_id}/{message_id}"

        return link


mention_service = MentionService()
