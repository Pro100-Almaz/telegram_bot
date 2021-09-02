from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from filters.private_chat import IsPrivate
from re import compile

from loader import dp
from utils.misc import rate_limit


@dp.message_handler(CommandStart(deep_link=compile(r"\d\d\d")), IsPrivate())
async def bot_start_deeplink(message: types.Message):

    deep_link_args = message.get_args()

    await message.answer(f'Hello, {message.from_user.full_name}!\n'
                         f'You are currently at direct messages\n'
                         f'You have deep link in you commands\n'
                         f'You have sended {deep_link_args}.\n')

@rate_limit(limit=10)
@dp.message_handler(CommandStart(), IsPrivate())
async def bot_start(message: types.Message):
    bot_user = await dp.bot.get_me()
    deep_link = f"http://t.me/{bot_user.username}?start=123"

    await message.answer(f'Hello, {message.from_user.full_name}!\n'
                         f'You are currently at direct messages\n'
                         f'You dont have deep link in you commands\n'
                         f'Your link to get it - {deep_link}.\n')