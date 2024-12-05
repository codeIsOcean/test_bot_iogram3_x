from aiogram.types import KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

# кроме обычного метода создания клавиатуры, в айограм есть еще один способ - через билдеры (builder)

data = ('Nike', 'Adidas', 'Reebok')


def brands():
    keyboard = ReplyKeyboardBuilder()
    for brand in data:
        keyboard.add(KeyboardButton(text=brand))
        return keyboard.adjust(2).as_markup()


# here we have to write text about the code
def code_is():
    for codes in code:
        new_variable = code + 1
