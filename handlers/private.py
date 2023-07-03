from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from database.utils import Utils


router = Router()
router.message.filter(F.chat.type =='private')

ut = Utils()


@router.message(Command(commands=["start"]))
async def cmd_start(message: Message) -> None:
    await message.answer(f"Hi, {message.from_user.full_name}!")


@router.message(Command(commands=["stats"]))
async def cmd_stats(message: Message):
    await message.answer(text=ut.give_statistics())
