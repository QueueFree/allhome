import logging
from aiogram import types
from aiogram.utils import executor
from config import bot, admin, dp
import commands, echo, quiz, fsm_reg, storage

async def on_startup(_):
    for i in admin:
        await bot.send_message(chat_id=i, text="Бот включен!")

commands.register_commands(dp)
quiz.register_quiz(dp)
fsm_reg.register_fsm_reg(dp)
storage.register_store(dp)

echo.register_echo(dp)


@dp.message_handler()
async def echo_handler(message: types.Message):
    await message.answer(message.text)

if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
