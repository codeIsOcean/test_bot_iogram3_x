from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

admin = Router()
@admin.message(Command('admin'))
async def cmd_apanel(message:Message):
    await message.answer('Это админ панель')
