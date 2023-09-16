import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from config_reader import config
from handlers import private, group


bot = Bot(config.token.get_secret_value(), parse_mode="HTML")


async def main() -> None:
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s")

    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router=private.router)
    dp.include_router(router=group.router)

    await bot.send_message(chat_id=config.destination_chat, text='Bot has started')
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
