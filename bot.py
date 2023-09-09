import asyncio

from aiogram import Bot, Dispatcher

from config_reader import config
from database.utils import Utils
from handlers import private, group


bot = Bot(config.token.get_secret_value(), parse_mode="HTML")
utils = Utils()


async def main() -> None:
    dp = Dispatcher()
    dp.include_router(router=private.router)
    dp.include_router(router=group.router)
    config.pattern = utils.make_pattern()

    await bot.send_message(chat_id=config.destination_chat, text='Bot has started')
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
