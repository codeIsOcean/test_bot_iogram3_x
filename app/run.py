import asyncio
import os

import logging
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

from app.handlers import router
from app.admin import admin

async def main():
    load_dotenv()
    bot = Bot(token=os.getenv('TOKEN'))
    dp = Dispatcher()
    dp.include_routers(router, admin)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')