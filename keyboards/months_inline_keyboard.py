from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder


class StatsPeriod(CallbackData, prefix="period"):
    value: int


def inline_months_keyboard(number: int):
    builder = InlineKeyboardBuilder()
    [builder.button(text=str(i), callback_data=StatsPeriod(value=i)) for i in range(1, number + 1)]

    return builder.as_markup()