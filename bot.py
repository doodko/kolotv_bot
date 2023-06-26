import asyncio
from re import Match

from aiogram import Bot, Dispatcher, Router, F
from aiogram.filters import Command
from aiogram.types import Message


TOKEN = "1145854936:AAFMrSy-0x7gUKuoD6VmcJcG5XDfYG6e4sI"
router = Router()
kolo = r".*(коло|[иі]нтернет|провайдер).*"
bot = Bot(TOKEN, parse_mode="HTML")


@router.message(Command(commands=["start"]))
async def cmd_start(message: Message) -> None:
    await message.answer(f"Hi, {message.from_user.full_name}!")


@router.message(F.text.lower().regexp(kolo))
async def ping_kivi(message: Message):
    # print(message.from_user.full_name, message.chat.title, message.from_user.id)
    # await message.send_copy(chat_id=7525617)
    await bot.send_message(chat_id=7525617, text=make_msg(
                                                user=message.from_user.full_name,
                                                chat=message.chat.title,
                                                text=message.text))


async def main() -> None:
    dp = Dispatcher()
    dp.include_router(router=router)
    await dp.start_polling(bot)


def make_msg(user, chat, text) -> str:
    return f"Pay attention to the <b>{chat}</b> chat, user {user} says:\n<b>{text}</b>"


if __name__ == "__main__":
    asyncio.run(main())
