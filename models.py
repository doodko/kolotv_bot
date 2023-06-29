from datetime import datetime

from sqlalchemy import String, ForeignKey, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Word(Base):
    __tablename__ = "word"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(10))

    def __repr__(self) -> str:
        return f"{self.name}"


class Chat(Base):
    __tablename__ = 'chat'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(20))
    link: Mapped[str] = mapped_column(String(20))

    def __repr__(self) -> str:
        return f"{self.name}"


class Match(Base):
    __tablename__ = 'match'

    id: Mapped[str] = mapped_column(primary_key=True)
    word_id: Mapped[int] = mapped_column(ForeignKey("word.id"))
    chat_id = Mapped[int] = mapped_column(ForeignKey("chat.id"))
    date: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())

    word: Mapped["Word"] = relationship()
    chat: Mapped["Chat"] = relationship()
