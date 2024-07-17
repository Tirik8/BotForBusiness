from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove

router = Router()


@router.message(Command("privacy"))
async def handler_command_start(message: Message):
    await message.answer(
        f"Политика конфиденциальности",
        reply_markup=ReplyKeyboardRemove(),
    )
