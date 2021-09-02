from aiogram.types import InlineKeyboardMarkup
from aiogram.types.inline_keyboard import InlineKeyboardButton
from .callback_data import buy_callback

choice = InlineKeyboardMarkup(row_width=2,inline_keyboard=[
                                [
                                InlineKeyboardButton(
                                    text="02",
                                    callback_data=buy_callback.new(item_name="zero_two",
                                                                    rating=8)
                                ),
                                InlineKeyboardButton(
                                    text="Mikasa",
                                    callback_data="waifu:mikasa:8"
                                ) ],
                                [InlineKeyboardButton(text="Cancel", callback_data="cancel")]
                                ]
                            )

zero_two_key = InlineKeyboardMarkup()

ZEROTWO_LINK = "https://mywaifulist.moe/waifu/zero-two-darling-in-the-franxx"

zerotwo_link = InlineKeyboardButton(text="Go to this site", url=ZEROTWO_LINK)

zero_two_key.insert(zerotwo_link)

mikasa_key = InlineKeyboardMarkup()

MIKASA_LINK = "https://mywaifulist.moe/waifu/mikasa-ackerman-attack-on-titan"

mikasa_link = InlineKeyboardButton(text="Go to this site", url=MIKASA_LINK)

mikasa_key.insert(mikasa_link)