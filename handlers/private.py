from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message


router = Router()
router.message.filter(F.chat.type =='private')


@router.message(Command(commands=["start"]))
async def cmd_start(message: Message) -> None:
    await message.answer(f"Hi, {message.from_user.full_name}!")


@router.message()
async def private_messages_handler(message: Message):
    await message.answer(text='okay')