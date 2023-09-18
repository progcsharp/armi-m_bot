import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import TOKEN
from lib.request import my_func
from register_handler.reg_commands import register_handlers_commands


async def main():
    bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)

    my_func()

    await register_handlers_commands(dp)

    await dp.start_polling()



if __name__ == '__main__':
    asyncio.run(main())

