from aiogram.dispatcher.filters import Command
from aiogram import types
from aiogram.types import CallbackQuery

from loader import dp
from keyboards.inline.choice import choice, zero_two_key, mikasa_key
from keyboards.inline.choice import buy_callback
from utils.misc.logging import logging

@dp.message_handler(Command("items"))
async def show_items(message:types.Message):
    await message.answer(text="Which waifu is better:", reply_markup=choice)

@dp.callback_query_handler(buy_callback.filter(item_name="zero_two"))
async def buying_zero_two(call:CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"callback_data dict = {callback_data}")
    rating = callback_data.get("rating")
    await call.message.answer(f"You have choisen 02. Her rating is {rating}. Thank you!", 
                                reply_markup=zero_two_key)

@dp.callback_query_handler(buy_callback.filter(item_name="mikasa"))
async def buying_mikasa(call:CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"callback_data dict = {callback_data}")
    rating = callback_data.get("rating")
    await call.message.answer(f"You have choisen Mikasa Akerman. Her rating is {rating}. Thank you!", 
                                reply_markup=mikasa_key)

@dp.callback_query_handler(text="cancel")
async def cancel(call: CallbackQuery):
    await call.answer("You calcelled your choice!", show_alert=True)
    await call.message.edit_reply_markup()