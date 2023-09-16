from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery

from keyboards.chats_inline_keyboard import chats_keyboard, ChatCallback
from keyboards.months_inline_keyboard import inline_months_keyboard, StatsPeriod
from services.mention_service import mention_service
from services.utils import utils

router = Router()
router.message.filter(F.chat.type =='private')


class Stats(StatesGroup):
    choosing_period = State()
    choosing_chat = State()


@router.message(Command(commands=["start"]))
async def cmd_start(message: Message) -> None:
    await message.answer(f"Hi, {message.from_user.full_name}!")


@router.message(Command(commands=["stats"]))
async def cmd_new(message: Message):
    await message.answer(text='За який період вибрати статистику?', reply_markup=inline_months_keyboard(6))


@router.callback_query(StatsPeriod.filter())
async def process_period(query: CallbackQuery, callback_data: StatsPeriod):
    months = callback_data.value
    stats = mention_service.give_statistics(months=months)

    await query.message.answer(text=stats.message, reply_markup=chats_keyboard(chat_list=stats.chats, period=months))
    await query.answer()


@router.callback_query(ChatCallback.filter())
async def process_chat(query: CallbackQuery, callback_data: ChatCallback):
    stats = mention_service.count_mentions_in_chat(chat_id=callback_data.id, months=callback_data.period)
    period_str = utils.get_month_string(number=callback_data.period)
    text = f"Такі пошукові слова зустрічались у чаті <b>{callback_data.title}</b> за <b>{period_str}</b>:\n\n{stats}"

    await query.message.answer(text=text)
    await query.answer()
