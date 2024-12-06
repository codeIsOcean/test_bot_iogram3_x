from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

router_state = Router()  # указываем имя роутера


# FSM Context
class Reg(StatesGroup):  # Reg имя класс создаем сами
    name = State()
    number = State()
    photo = State()


@router_state.message(CommandStart())
async def c_start(message: Message, state: FSMContext):
    await state.set_state(Reg.name)  # Установка состояния
    await message.answer(f'Привет! Введите свое имя')


@router_state.message(Reg.name)
async def reg_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)  # Вся информация, присланная пользователем сохраняется
    # в метод state.update_data и ему даётся какой-либо ключ.
    await state.set_state(Reg.number)  # устанавливаем следующий статус для получения номера телефона
    await message.answer('Отправьте свой номер телефона')


@router_state.message(Reg.number)
async def reg_number(message: Message, state: FSMContext):
    await state.update_data(number=message.text)
    await state.set_state(Reg.photo)
    await message.answer('Отправьте фото')


@router_state.message(Reg.photo)
async def reg_photo(message: Message, state: FSMContext):
    await state.update_data(photo=message.photo[-1].file_id)
    data = await state.get_data()  # получаем информацию, полученную от пользователя
    await message.answer_photo(photo=data['photo'],
                               caption=f'Информация о Вас: {data['name']}, {data['number']}')

