import asyncio
import os

import logging
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

from app.handlers import router
from app.admin import admin
from app.handlers_admin.warnings import w_router
from app.states import router_state


async def main():
    load_dotenv()
    bot = Bot(token=os.getenv('TOKEN'))
    dp = Dispatcher()
    dp.include_routers(router_state)
    dp.include_router(w_router)
    dp.include_routers(admin, router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
