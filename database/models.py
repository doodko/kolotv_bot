from datetime import datetime

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
    chat_id: Mapped[int] = mapped_column(Integer)
    link: Mapped[str] = mapped_column(String(25))

    mentioned_word: Mapped["Word"] = relationship(back_populates="mentions")

    def __repr__(self) -> str:
        return f"{self.date} - {self.mentioned_word}"

class Chat(Base):
    __tablename__ = 'chat'

    chat_id: Mapped[int] = mapped_column(Integer)
    chat_name: Mapped[str] = mapped_column(String(50))

    def __repr__(self) -> str:
        return f"{self.chat_name}"
