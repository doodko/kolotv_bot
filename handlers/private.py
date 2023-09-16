from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery

from keyboards.months_inline_keyboard import inline_months_keyboard, StatsPeriod
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
async def cmd_stats(message: Message):
    await message.answer(text=utils.give_statistics())


@router.message(Command(commands=["new"]))
async def cmd_new(message: Message, ):
    await message.answer(text='За який період?', reply_markup=inline_months_keyboard(6))


@router.callback_query(StatsPeriod.filter(F.value > 0))
async def process_period(query: CallbackQuery):
    answer = f"Вибрано період {query.data} місяців"
    await query.message.answer(text=answer)
    await query.answer()
