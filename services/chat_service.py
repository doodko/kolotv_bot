from aiogram.types import Chat as ChatType

from database.db import Session
from database.models import Chat


class ChatService:
    def __init__(self, session: Session = Session()):
        self.session = session

    def create_chat_or_update_title(self, tg_chat: ChatType):
        chat = self.session.query(Chat).filter(Chat.id == tg_chat.id).first()

        if not chat:
            chat = Chat(id=tg_chat.id, title=tg_chat.title)
            self.session.add(chat)
            self.session.commit()

        if tg_chat.title != chat.title:
            chat.title = tg_chat.title
            self.session.commit()

    def get_all_chats(self) -> list[Chat]:
        return self.session.query(Chat).all()

    def get_chat_by_id(self, chat_id: int) -> Chat:
        return self.session.query(Chat).filter(Chat.id == chat_id).first()

    def get_chat_title(self, chat_id: int) -> str:
        chat = self.get_chat_by_id(chat_id=chat_id)
        if not chat:
            return 'Unknown chat'
        return chat.title



chat_service = ChatService()
