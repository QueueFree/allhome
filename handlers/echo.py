from aiogram import types, Dispatcher
from config import bot

games = ['⚽', '🎰', '🏀', '🎯', '🎳']

async def echo_handler(message: types.Message):
    if message.text == '/dice':
        await bot.send_dice(emoji='🎲', chat_id=message.from_user.id)
    elif message.text == '/games':
        for i in games:
            await bot.send_dice(emoji=i, chat_id=message.from_user.id)
    else:
        await message.answer(message.text)


def register_echo(dp: Dispatcher):
    dp.register_message_handler(echo_handler)
