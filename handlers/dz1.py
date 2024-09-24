import logging
from aiogram import types
from aiogram.utils import executor
from config import bot, admin, dp
import commands, echo, quiz, fsm
from allhome.db import db_main
from buttons import start_test
import webapp

async def on_startup(_):
    for i in admin:
        await bot.send_message(chat_id=i, text="Бот включен!",
                               reply_markup=start_test)
        await db_main.sql_create()

commands.register_commands(dp)
quiz.register_quiz(dp)
fsm.register_store(dp)
webapp.register_handlers_webapp(dp)

echo.register_echo(dp)

@dp.message_handler()
async def echo_handler(message: types.Message):
    await message.answer(message.text)

if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
