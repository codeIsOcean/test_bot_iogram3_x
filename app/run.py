import asyncio
import os

import logging
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

from app.handlers import router
from app.admin import admin
from app.handlers_admin.warnings import wrouter


async def main():
    load_dotenv()
    bot = Bot(token=os.getenv('TOKEN'))
    dp = Dispatcher()
    dp.include_router(wrouter)
    dp.include_routers(admin, router)
   
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')