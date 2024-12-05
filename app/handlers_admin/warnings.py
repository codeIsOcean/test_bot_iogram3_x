import asyncio  # Для работы с асинхронным кодом
from aiogram import Bot, Dispatcher, Router  # Основные классы для бота, диспетчера и роутера
from aiogram.filters import Command  # Фильтр для обработки команд
from aiogram.types import Message  # Класс для работы с сообщениями
from aiogram.exceptions import TelegramAPIError  # Исключения Telegram API
from aiogram.filters import CommandObject  # Для получения аргументов команды

# Создаем экземпляр роутера
w_router = Router()


# Обработчик команды /warn
@w_router.message(Command(commands=["warn"]))  # Используем фильтр Command для команды warn
async def warn_user(message: Message, command: CommandObject):
    """
    Обработчик команды /warn.
    """
    try:
        # Удаляем сообщение с командой
        await message.delete()

        # Проверяем, ответил ли админ на сообщение
        if not message.reply_to_message:
            await message.answer("Эта команда должна быть ответом на сообщение. обязательно дела")
            return

        # Удаляем сообщение пользователя, на которое ответил админ
        await message.reply_to_message.delete()

        # Отправляем предупреждение пользователю
        user = message.reply_to_message.from_user
        admin = message.from_user
        user_mention = f'<a href="tg://user?id={user.id}">{user.full_name}</a>'
        admin_mention = f'<a href="tg://user?id={admin.id}">{admin.full_name}</a>'
        warning_message = await message.answer(
            f"⚠️ {user_mention}, вы были предупреждены администратором {admin_mention}.",
            parse_mode="HTML"
        )

        # Удаляем предупреждение через 10 секунд
        await asyncio.sleep(10)
        await warning_message.delete()

    except TelegramAPIError as e:
        # Обработка ошибок Telegram API
        await message.answer(f"Ошибка Telegram API: {e}")
    except Exception as e:
        # Обработка остальных ошибок
        await message.answer(f"Произошла ошибка: {e}")
