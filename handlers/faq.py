from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

router = Router()
router.message.filter(F.chat.type =='private')


@router.message(Command(commands=["start"]))
async def cmd_start(message: Message) -> None:
    msg = f"Привіт, {message.from_user.full_name}! Для зв'язку з підтримкою прохання звертатись в чат-бот: @kolotv_bot"
    await message.answer(msg)


@router.message()
async def all_other_messages(message: Message) -> None:
    print(message.from_user)
    await message.answer("Для зв'язку з підтримкою прохання звертатись в чат-бот: @kolotv_bot")
