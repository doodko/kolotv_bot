from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from config_reader import config
from keyboards.chats_inline_keyboard import chats_keyboard, ChatCallback
from keyboards.months_inline_keyboard import inline_months_keyboard, StatsPeriod
from services.chat_service import chat_service
from services.mention_service import mention_service
from services.utils import utils

router = Router()
router.message.filter((F.chat.type =='private') & F.from_user.id.in_(config.admins))


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
    chat_title = chat_service.get_chat_title(chat_id=callback_data.id)
    text = f"Такі пошукові слова зустрічались у чаті <b>{chat_title}</b> за <b>{period_str}</b>:\n\n{stats}"
    mention_service.export_mentions_to_csv(chat_id=callback_data.id)

    await query.message.answer(text=text)
    await query.answer()
