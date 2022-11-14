from aiogram import Bot, executor, Dispatcher, types
from aiogram.types import base, InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from decouple import config


TOKEN = config("TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)



@dp.message_handler(commands=['start'])
async def hello(message: types.Message):
    await bot.send_message(message.chat.id, f'Hello : {message.from_user.full_name}')


# 1
@dp.message_handler(commands=['games'])
async def games_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("Следующая задача",
                                         callback_data='next_task1')
    markup.add(button_call_1)
    question = 'Какой национальный цветок Японии?'
    answers = ['Ромашка', 'Роза', 'Сакура', 'Пионы']
    photo = open('media/sakura.jpeg', 'rb')
    await bot.send_photo(message.chat.id, photo=photo)
    await bot.send_poll(
        message.chat.id,
        question=question,
        options=answers,
        correct_option_id=3,
        is_anonymous=False,
        type='quiz',
        reply_markup=markup,
        open_period=30,
        explanation='Это очень легкий вопрос, подумай хорошо',
        explanation_parse_mode=ParseMode.MARKDOWN_V2
    )


# 2
@dp.callback_query_handler(lambda func: func.data == 'next_task1')
async def games_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton('Следующая задача', callback_data='next_task2')
    markup.add(button_call_2)
    question2 = 'Сколько полос на флаге США?'
    answers = ['10', '7', '12', '13']
    photo = open('media/usa.png', 'rb')
    await bot.send_photo(call.message.chat.id, photo=photo)
    await bot.send_poll(
        call.message.chat.id,
        question=question2,
        options=answers,
        correct_option_id=4,
        open_period=30,
        explanation='Посчитай',
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        is_anonymous=False,
        type='quiz',
        reply_markup=markup
    )


# 3
@dp.callback_query_handler(lambda func: func.data == 'next_task2')
async def task_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_3 = InlineKeyboardButton("Следующая задача", callback_data='next_task3')
    markup.add(button_call_3)
    question3 = 'Какое нацональное животное Австралии?'
    answers3 = ['Зебра', 'Кенгуру', 'Паук', 'Жираф']
    photo = open('media/kenguru.jpeg', 'rb')
    await bot.send_photo(call.message.chat.id, photo=photo)
    await bot.send_poll(
        call.message.chat.id,
        question=question3,
        options=answers3,
        correct_option_id=2,
        open_period=30,
        explanation='Он моеж тебя побить',
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        is_anonymous=False,
        type='quiz',
        reply_markup=markup
    )


# 4
@dp.callback_query_handler(lambda func: func.data == 'next_task3')
async def task_4(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_4 = InlineKeyboardButton("Следующая задача", callback_data='next_task4')
    markup.add(button_call_4)
    question4 = 'Из какого зерна делается японский спирт саке?'
    answers4 = ['Рис', 'Пщеница', 'Горох']
    photo = open('media/rice.jpeg', 'rb')
    await bot.send_photo(call.message.chat.id, photo=photo)
    await bot.send_poll(
        call.message.chat.id,
        question=question4,
        options=answers4,
        correct_option_id=1,
        open_period=30,
        explanation='Сушии',
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        is_anonymous=False,
        type='quiz',
        reply_markup=markup
    )


@dp.callback_query_handler(lambda func: func.data == 'next_task4')
async def task_5(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_5 = InlineKeyboardButton("Следующая задача", callback_data='next_task5')
    markup.add(button_call_5)
    question5 = 'До 1923 года как назывался турецкий город Стамбул?'
    answers5 = ['Константинополь', 'Бурса', 'Измир']
    photo = open('media/turkey.png', 'rb')
    await bot.send_photo(call.message.chat.id, photo=photo)
    await bot.send_poll(
        call.message.chat.id,
        question=question5,
        options=answers5,
        correct_option_id=1,
        open_period=30,
        explanation='Самый длинный ответ',
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        is_anonymous=False,
        type='quiz',
        reply_markup=markup
    )


@dp.callback_query_handler(lambda func: func.data == 'next_task5')
async def task_6(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_5 = InlineKeyboardButton("Следующая задача", callback_data='next_task6')
    markup.add(button_call_5)
    question5 = 'Что означает www в браузере веб-сайтов?'
    answers5 = ['пин код', 'всемирная поутина', 'обхват']
    photo = open('media/www.jpeg', 'rb')
    await bot.send_photo(call.message.chat.id, photo=photo)
    await bot.send_poll(
        call.message.chat.id,
        question=question5,
        options=answers5,
        correct_option_id=2,
        open_period=30,
        explanation='погугли',
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        is_anonymous=False,
        type='quiz',
        reply_markup=markup
    )



if __name__ == "__main__":
	executor.start_polling(dp, skip_updates=False)
