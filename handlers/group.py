from aiogram import Router, F
from aiogram.types import Message

from bot import bot
from config_reader import config

router = Router()
router.message.filter(F.chat.type == 'supergroup')

alert_list = r".*(коло|[иі]нтернет|провайдер).*"


@router.message(F.text.lower().regexp(alert_list))
async def ping_kivi(message: Message):
    await bot.send_message(chat_id=config.superuser_id, text=make_msg(
                                                user=message.from_user.full_name,
                                                chat=message.chat.title,
                                                text=message.text))


def make_msg(user, chat, text) -> str:
    return f"Pay attention to the <b>{chat}</b> chat, user {user} says:\n<b>{text}</b>"
