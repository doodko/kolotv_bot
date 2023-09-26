import asyncio
import logging

from aiogram import Bot, Dispatcher

from config_reader import config
from handlers import statistics, group, faq
from services.utils import utils

bot = Bot(config.token.get_secret_value(), parse_mode="HTML")


async def main() -> None:
    # logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(name)s - %(message)s")

    dp = Dispatcher()
    dp.include_router(router=group.router)
    dp.include_router(router=statistics.router)
    dp.include_router(router=faq.router)

    config.pattern = utils.make_pattern()

    await bot.send_message(chat_id=config.destination_chat, text='Bot has started')
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
