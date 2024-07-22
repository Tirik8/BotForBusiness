from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove

router = Router()


@router.message(Command("privacy"))
async def handler_command_start(message: Message):
    await message.answer(
        f"Политика конфиденциальности\n\n",
        f"Сервис хранит информацию о пользователях, подключивших его, на протяжении всего сипользования и 30 дней после отключения от сервиса",
        
        reply_markup=ReplyKeyboardRemove(),
    )
