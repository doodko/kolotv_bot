from aiogram.types import Chat as ChatType

from database.db import Session
from database.models import Chat


class ChatService:
    def __init__(self, session: Session = Session()):
        self.session = session

    def create_chat_or_update_title(self, tg_chat: ChatType):
        chat = self.session.query(Chat).filter(Chat.id == tg_chat.id).first()

        if not chat:
            chat = Chat(id=tg_chat.id, chat_name=tg_chat.title)
            self.session.add(chat)
            self.session.commit()

        if tg_chat.title != chat.chat_name:
            chat.chat_name = tg_chat.title
            self.session.commit()

    def get_all_chats(self) -> list[Chat]:
        return self.session.query(Chat).all()


chat_service = ChatService()
