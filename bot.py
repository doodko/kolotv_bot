import asyncio

from aiogram import Bot, Dispatcher, Router, F
from aiogram.filters import Command
from aiogram.types import Message

from config_reader import config


bot = Bot(config.token.get_secret_value(), parse_mode="HTML")
router = Router()
kolo = r".*(коло|[иі]нтернет|провайдер).*"


@router.message(Command(commands=["start"]))
async def cmd_start(message: Message) -> None:
    await message.answer(f"Hi, {message.from_user.full_name}!")


@router.message(F.text.lower().regexp(kolo))
async def ping_kivi(message: Message):
    await bot.send_message(chat_id=config.superuser_id, text=make_msg(
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
