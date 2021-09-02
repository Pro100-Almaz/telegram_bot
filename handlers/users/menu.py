from aiogram import types
from aiogram.types.reply_keyboard import ReplyKeyboardRemove
from loader import dp 
from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from keyboards.default import menu

@dp.message_handler(Command("menu"))
async def show_menu(message:types.Message):
    await message.answer("Choose smth from list bellow", reply_markup=menu)

@dp.message_handler(text="1")
async def get_kotletki(message:types.Message):
    await message.answer("You choise was 1")

@dp.message_handler(Text(equals=["2","3"]))
async def get_food(message:types.Message):
    await message.answer(f"You choise was {message.text}", reply_markup=ReplyKeyboardRemove())
