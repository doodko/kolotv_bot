from datetime import datetime

from pydantic import BaseModel
from sqlalchemy import String, ForeignKey, DateTime, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)


class Word(Base):
    __tablename__ = "word"

    name: Mapped[str] = mapped_column(String(10))
    pattern: Mapped[str] = mapped_column(String(20))

    mentions: Mapped[list["Mention"]] = relationship(back_populates="mentioned_word")

    def __repr__(self) -> str:
        return f"{self.name}"


class Mention(Base):
    __tablename__ = 'mention'

    date: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    word_id: Mapped[int] = mapped_column(ForeignKey("word.id"))
    chat_id: Mapped[int] = mapped_column(ForeignKey("chat.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    text: Mapped[str] = mapped_column(String)
    link: Mapped[str] = mapped_column(String)

    mentioned_word: Mapped["Word"] = relationship(back_populates="mentions")

    def __repr__(self) -> str:
        return f"{self.date} - {self.mentioned_word}"

class Chat(Base):
    __tablename__ = 'chat'

    title: Mapped[str] = mapped_column(String(50))

    def __repr__(self) -> str:
        return f"{self.title}"

class User(Base):
    __tablename__ = 'users'

    full_name: Mapped[str] = mapped_column(String)
    nickname: Mapped[str] = mapped_column(String, nullable=True)

    def __repr__(self) -> str:
        return f"{self.full_name if self.full_name else self.id}"



class MessageWithChats(BaseModel):
    message: str
    chats: list