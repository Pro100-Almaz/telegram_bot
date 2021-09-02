from aiogram.types import ReplyKeyboardMarkup
from aiogram.types.reply_keyboard import KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1")
        ],
        [KeyboardButton(text="2")],
        [KeyboardButton(text="3")]
    ],
    resize_keyboard=True
)