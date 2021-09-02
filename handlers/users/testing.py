from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.storage import FSMContext

from loader import dp 
from aiogram import types

from states import Test
import states

@dp.message_handler(Command("test"))
async def enter_test(message: types.Message):
    await message.answer("You have started testing.\n"
                         "Question No.1\n\n"
                         "Are you studing after 11pm?\n"
                         "(It might assumed as self development stuff, course homework or smt-g like that)")

    await Test.Q1.set()

@dp.message_handler(state=Test.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer1=answer)

    await message.answer("Question No.2\n\n"
                         "Do you have depression?")
    await Test.Q2.set()

@dp.message_handler(state=Test.Q2)
async def answer_q2(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer1 = data.get("answer1")
    answer2 = message.text

    await message.answer("Thank you for your response\n")
    await message.answer(f"Answer 1:{answer1}")
    await message.answer(f"Answer 2:{answer2}")

    await state.finish()
    await state.reset_state(with_data=True)
