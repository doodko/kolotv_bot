from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton

from database.models import Chat


class ChatCallback(CallbackData, prefix="chat"):
    period: int
    id: int


def chats_keyboard(chat_list: list[Chat], period: int):
    builder = InlineKeyboardBuilder()

    for chat in chat_list:
        callback_data = ChatCallback(period=period, id=chat.id)
        builder.button(text=chat.title, callback_data=callback_data)

    builder.adjust(1)
    return builder.as_markup()
