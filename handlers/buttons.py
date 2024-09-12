from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start = ReplyKeyboardMarkup(resize_keyboard=True,
                            row_width=2)

start_buttons = KeyboardButton('/start')
mem_buttons = KeyboardButton('/mem_handler')
mem_all_buttons = KeyboardButton('/mem_all')
music_buttons = KeyboardButton('/music')
quiz_buttons = KeyboardButton('/quiz')
dice_buttons = KeyboardButton('/dice')
games_buttons = KeyboardButton('/games')


start.add(start_buttons, mem_buttons, mem_all_buttons, music_buttons, quiz_buttons, dice_buttons, games_buttons)

start_test = ReplyKeyboardMarkup(
    resize_keyboard=True,
    row_width=2
    ).add(
    KeyboardButton('/start'),
    KeyboardButton('mem'),
    KeyboardButton('/mem_all'),
    KeyboardButton('/music'),
    KeyboardButton('/quiz'),
    KeyboardButton('/dice'),
    KeyboardButton('/games')
)
