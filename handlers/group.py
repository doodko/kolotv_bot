from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot import bot
from config_reader import config


router = Router()

alert_list = r".*(коло|[иі]нтернет|провайдер).*"


@router.message(F.text.lower().regexp(alert_list))
async def ping_kivi(message: Message):
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="Jump to message", url=make_msg_link(message)))

    await bot.send_message(chat_id=config.superuser_id, text=make_msg(message), reply_markup=builder.as_markup())


def make_msg(message: Message) -> str:
    chat_name = message.chat.title
    user = message.from_user.full_name

    return f"{user} in the <b>{chat_name}</b> chat says:\n<i>{message.text}</i>"


def make_msg_link(message: Message) -> str:
    chat_id = message.chat.username or (message.chat.id + 1000000000000) * -1
    message_id = message.message_id
    link = f"https://t.me/c/{chat_id}/{message_id}"

    return link
