import asyncio

from aiogram import Bot, Dispatcher

from config_reader import config
from handlers import private, group
from services.utils import utils


bot = Bot(config.token.get_secret_value(), parse_mode="HTML")


async def main() -> None:
    dp = Dispatcher()
    dp.include_router(router=private.router)
    dp.include_router(router=group.router)

    await bot.send_message(chat_id=config.destination_chat, text='Bot has started')
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    config.pattern = utils.make_pattern()
    asyncio.run(main())
