from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardButton, InlineKeyboardMarkup)

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Каталог'),
     KeyboardButton(text='Корзина')],
    [KeyboardButton(text='Контакты', request_contact=True)]
],
    resize_keyboard=True,
    input_field_placeholder='Выберите пункт меню')

# main_inline = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='Написать Мне', url='https://t.me/kanich07'),
#      InlineKeyboardButton(text='Написать Тебе', url='https://t.me/kair_kairov')],
#     [InlineKeyboardButton(text='Написать Им', url='https://t.me/thebest78')]
# ])

main_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Напишите мне', callback_data='write_me'),
     InlineKeyboardButton(text='Написать тебе', callback_data='write_you')],
    [InlineKeyboardButton(text='Написать Им', callback_data='write_them')]
])
