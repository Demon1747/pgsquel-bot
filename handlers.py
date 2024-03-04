from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Привет! Я помогу тебе узнать твою ориентацию!")


@router.message()
async def message_handler(msg: Message):
    await msg.answer(f"{msg.from_user.first_name}, ты пидор!")
