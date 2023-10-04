import os
import re
import csv
from datetime import datetime

from aiogram.types import Message
from sqlalchemy import func

from database.db import Session
from database.models import Mention, Word, Chat, MessageWithChats, User
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

        mentions = [Mention(
                        date=datetime.now(),
                        word_id=word.id,
                        chat_id=message.chat.id,
                        link=link,
                        user_id=message.from_user.id,
                        text=message.text)
                    for word in words]

        self.session.add_all(mentions)
        self.session.commit()

    def give_statistics(self, months: int = 1) -> MessageWithChats:
        chats = (self.session.query(Chat)
                    .join(Mention, Chat.id == Mention.chat_id)
                    .filter(Mention.date >= utils.months_ago(months=months))
                    .all())

        words_counts = self.count_mentions(months=months)
        msg = (f"За період <b>{utils.get_month_string(number=months)}</b> пошукові слова зустрічались "
               f"у <b>{len(chats)}</b> чатах.\n\n"
               f"Найчастіше згадують:\n{words_counts}")

        return MessageWithChats(message=msg, chats=chats)

    def count_mentions(self, months: int = 1) -> str:
        words_counts = (self.session.query(Word.name, func.count(Mention.id))
                        .join(Word.mentions)
                        .filter(Mention.date >= utils.months_ago(months=months))
                        .group_by(Word.name)
                        .order_by(func.count(Mention.id)
                        .desc()).all())

        words_string = '\n'.join([f"{word}: {count}" for word, count in words_counts])
        return words_string

    def count_mentions_in_chat(self, chat_id: int, months: int = 1) -> str:
        words_counts = (self.session.query(Word.name, func.count(Mention.id))
                        .join(Word.mentions)
                        .filter(Mention.date >= utils.months_ago(months=months))
                        .filter(Mention.chat_id == chat_id)
                        .group_by(Word.name)
                        .order_by(func.count(Mention.id)
                        .desc()).all())

        words_string = '\n'.join([f"{word}: {count}" for word, count in words_counts])
        return words_string

    def export_mentions_to_csv(self, chat_id: int) -> str:
        export_directory = "files"
        os.makedirs(export_directory, exist_ok=True)
        csv_file_path = os.path.join(export_directory, f"chat{chat_id}.csv")

        mentions = self.session.query(Mention).filter_by(chat_id=chat_id).all()

        with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=';')
            csv_writer.writerow(["datetime", "user", "text", "link"])

            for mention in mentions:
                user = self.session.get(User, mention.user_id)
                csv_writer.writerow([mention.date, user.full_name, mention.text, mention.link])

        return csv_file_path


mention_service = MentionService()
