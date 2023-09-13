from aiogram import Router, F
from aiogram.filters import ChatMemberUpdatedFilter, IS_NOT_MEMBER, MEMBER
from aiogram.types import Message, InlineKeyboardButton, ChatMemberUpdated
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot import bot
from config_reader import config
from filters.kolo_handler import KoloFilter
from services.mention_service import mention_service
from services.utils import utils


router = Router()
router.message.filter(F.chat.type.in_({'group', 'supergroup'}))


@router.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=IS_NOT_MEMBER >> MEMBER))
async def bot_added_as_member(event: ChatMemberUpdated):
    text = f'Bot was added to the chat <b>{event.chat.title}</b>'
    link = f"https://t.me/c/{utils.get_full_chat_id(chat_id=event.chat.id)}"

    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="Jump to chat", url=link))

    await bot.send_message(chat_id=config.destination_chat, text=text, reply_markup=builder.as_markup())


@router.message(KoloFilter())
async def ping_kolo(message: Message):
    word_list = mention_service.get_mentions_list(message=message)
    mention_service.add_mentions(words=word_list, message=message)

    words = ', '.join([mention.name for mention in word_list])
    text =  f"{message.from_user.full_name} in <b>{message.chat.title}</b> chat mentioned <b>{words}</b>:\n\n<i>{message.text}</i>"
    link = f"https://t.me/c/{utils.get_full_chat_id(chat_id=message.chat.id)}/{message.message_id}"

    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="Jump to message", url=link))

    await bot.send_message(chat_id=config.destination_chat, text=text, reply_markup=builder.as_markup())
