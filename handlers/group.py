import re

from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot import bot
from config_reader import config
from services.mention_service import mention_service
from services.word_service import word_service

router = Router()


@router.message(lambda message: re.search(config.pattern, message.text, re.IGNORECASE))
async def ping_kolo(message: Message):
    mention_service.add_new_mention(message)
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="Jump to message", url=make_msg_link(message)))

    await bot.send_message(chat_id=config.destination_chat, text=make_msg(message), reply_markup=builder.as_markup())


def make_msg(message: Message) -> str:
    chat_name = message.chat.title
    user = message.from_user.full_name
    words = [word.name for word in word_service.get_all_words() if re.search(word.pattern, message.text.lower())]

    return f"{user} in <b>{chat_name}</b> chat mentioned <b>{', '.join(words)}</b>:\n\n<i>{message.text}</i>"


def make_msg_link(message: Message) -> str:
    chat_id = (message.chat.id + 1000000000000) * -1
    message_id = message.message_id
    link = f"https://t.me/c/{chat_id}/{message_id}"

    return link
