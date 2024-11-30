import asyncio
from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandObject
from aiogram.filters import Command
from aiogram.filters import CommandStart
from aiogram.enums import ChatAction  # показывает что бот якобы пишет и отвечает

import app.keyboards as kb
import app.keyboards as kb_inline


router = Router()


@router.message(CommandStart())  # диспетчер проверяет являться ли команда командой старт
async def cmd_start(message: Message):
    await message.bot.send_chat_action(chat_id=message.from_user.id, action=ChatAction.TYPING)
    await asyncio.sleep(5)
    await message.answer(text='Hello dear, I am a Bot', reply_markup=kb.main) # сюда вложили клавиатуру, клавиатура крепиться к определенному сообщению
    await message.reply('Я отвечаю как дела на твое смс')
    
@router.message(Command('test'))
async def group_test(message:Message):
    await message.bot.send_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, text=f'Отвечаю вам Фак офф')


@router.callback_query(F.data == 'write_me')
async def cmd_write_me(callback:CallbackQuery):
    await callback.answer('Ты! открыл каталог write_me, bye')
    await callback.message.answer('Вы открыли write_me')
    

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer(f'{message.from_user.first_name}, вам нужна помошь?', reply_markup=kb_inline.main_inline)


# # CommandObject
# @router.message(Command('get'))
# async def cmd_get(message:Message, command: CommandObject):
#     await message.answer(f'Вы ввели команду get с аргументом {command.args}')


# Можно принимать несколько обьектов
@router.message(Command('get'))
async def cmd_get_two(message: Message, command: CommandObject):
    if not command.args:
        await message.answer('Аргументы не переданы')
        return
    try:
        value1, value2 = command.args.split(' ', maxsplit=1)
        await message.answer(f'Вы ввели команду "get" с аргументом {value1} {value2}')
    except ValueError:
        await message.answer('Были введены не правильные аргументы')


@router.message(F.text == 'Привет')  # этот обработчик ловит все смс пустой фильтр только используем в конце
async def echo(message: Message):
    await message.answer('Привет ты написал Ф ')
    await message.reply('Я отвечаю тебе с попошью Ф')
    await message.answer(f'Your user id: {message.from_user.id}')


# @router.message(F.photo)
# async def echo(message:Message):
#     photo_id = message.photo[-1].file_id
#     await message.answer_photo(photo=photo_id)


@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f'ID фотографий: {message.photo[-1].file_id}')


@router.message(F.document)
async def echo_document(message: Message):
    await message.answer_document(document=message.document.file_id)


@router.message(F.audio)
async def echo_audio(message: Message):
    await message.answer_audio(audio=message.audio.file_id)


@router.message(F.voice)
async def echo_voice(message: Message):
    await message.answer_voice(voice=message.voice.file_id)


@router.message(F.animation)
async def echo_animation(message: Message):
    await message.answer_animation(animation=message.animation.file_id)
    await message.answer('Your send an animation')


@router.message(F.from_user.id == 1942053951)
async def echo_from_user(message: Message):
    await message.answer(f'Written the user with ID: {message.from_user.id}')


@router.message()
async def log_message(message: Message):
    print(f'receive message:{message}')