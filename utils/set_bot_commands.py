from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Bot Activation"),
        types.BotCommand("help", "Need help"),
        types.BotCommand("test", "Testing you"),
        types.BotCommand("items", "Make you choise"),
        types.BotCommand("menu", "Check some Buttons"),
    ])
