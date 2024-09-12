from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot


async def quiz_handler(message: types.Message):
    quiz_button = InlineKeyboardMarkup()
    quiz_1_button = InlineKeyboardButton('Дальше...',
                                         callback_data='button_1')
    quiz_button.add(quiz_1_button)

    question = 'Сколько лет в среднем живут мужчины?'
    answer = ['13', '43', '96', '38', '66', '62']

    await bot.send_poll(
     chat_id=message.from_user.id,
     question=question,
     options=answer,
     is_anonymous=False,
     type='quiz',
     correct_option_id=4,
     explanation='в среднем 66 лет',
     open_period=60,
     reply_markup=quiz_button
    )

async def quiz_2(message: types.Message):
    quiz_button2 = InlineKeyboardMarkup()
    quiz_2_button = InlineKeyboardButton('Дальше...',
                                         callback_data='button_2')
    quiz_button2.add(quiz_2_button)

    question = 'Хорошо, какие три принципа ООП?'
    answer = ['классы, конструктор, метод', "инкапсуляция, полиморфизм, наследование", "функции, переменные, алгоритмы"]

    await bot.send_poll(
     chat_id=message.from_user.id,
     question=question,
     options=answer,
     is_anonymous=False,
     type='quiz',
     correct_option_id=1,
     explanation='инкапсуляция, полиморфизм, наследование - основа ооп',
     open_period=60,
     reply_markup=quiz_button2
    )

async def quiz_3(message: types.Message):
    quiz_button3 = InlineKeyboardMarkup()
    quiz_4_button = InlineKeyboardButton('Дальше...',
                                         callback_data='button_3')
    quiz_button3.add(quiz_4_button)

    question = 'как будет "Северное сияние" на Латыни?'
    answer = ['Deroa Vitchinus', 'Seronia Liazius', 'Aurora Borealis']

    await bot.send_poll(
     chat_id=message.from_user.id,
     question=question,
     options=answer,
     is_anonymous=False,
     type='quiz',
     correct_option_id=2,
     explanation='',
     open_period=60,
     reply_markup=quiz_button3
    )


async def quiz_4(message: types.Message):
    quiz_button4 = InlineKeyboardMarkup()
    quiz_5_button = InlineKeyboardButton('Дальше...',
                                         callback_data='button_4')
    quiz_button4.add(quiz_5_button)

    question = 'Где родился Наполеон Бонапарт?'
    answer = ["Париж", "Тулон", "Кёльн", "Аяччо"]

    await bot.send_poll(
     chat_id=message.from_user.id,
     question=question,
     options=answer,
     is_anonymous=False,
     type='quiz',
     correct_option_id=3,
     explanation='Наполеон родился на Острове Корсика в городе Аяччо, был по нации Корсиканцем',
     open_period=60,
     reply_markup=quiz_button4
    )

async def quiz_5(message: types.Message):
    quiz_button5 = InlineKeyboardMarkup()
    quiz_6_button = InlineKeyboardButton('Дальше...',
                                         callback_data='button_5')
    quiz_button5.add(quiz_6_button)

    question = 'Чему равно число Пи?'
    answer = ["2.12", "3.14", "18.01", "7.37"]

    await bot.send_poll(
     chat_id=message.from_user.id,
     question=question,
     options=answer,
     is_anonymous=False,
     type='quiz',
     correct_option_id=1,
     explanation='Наполеон родился на Острове Корсика в городе Аяччо, был по нации Корсиканцем',
     open_period=60,
     reply_markup=quiz_button5
    )

def register_quiz(dp: Dispatcher):
    dp.register_message_handler(quiz_handler, commands=['quiz'])
    dp.register_callback_query_handler(quiz_2, text='button_1', )
    dp.register_callback_query_handler(quiz_3, text='button_2', )
    dp.register_callback_query_handler(quiz_4, text='button_3', )
    dp.register_callback_query_handler(quiz_5, text='button_4', )
