import telebot
from telebot import types

bot = telebot.TeleBot('1770273344:AAE-ysvlrSWEeuZ0QqgRyZp9zDs_GZ6PIL4')

days = {'понедельник':'1. Русский\n2. Инф. и ИКТ\n3. Английский язык\n4. Английский язык\n5. Биология\n6. География',
        'вторник':'1. Алгебра\n2. Алгебра\n3. Проектная деятельность\n4. Физика\n5. Физика\n6. Литература',
        'среда':'1. Физика\n2. Техногология\n 3. Русский язык\n4. Литература\n5. История\n6. Обществознание',
        'четверг':'1. Геометрия\n2. Русский язык\n3. Английский язык\n4. Музыка\n5. Геометрия\n6. Русский язык',
        'пятница':'1. Алгебра\n2. Алгебра\n3. История\n4. Физкультура\n5. Физкультура\n6. Физкультура',
        'суббота':'1. Музыка\n2. География\n3. Алгебра\n4. Алгебра\n5. Английский язык'}

markup_main_menu = types.ReplyKeyboardMarkup(True)
markup_main_menu.row('Расписание')

def get_data(count=None):
    for day in days:
        return f'{day.capitalize()}:\n{days[day]}\n'


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.from_user.id, f'Привет, я бот Олег, если хочешь узнать расписание на завтра пиши '
                                           f'"расписание", если вы хотите добавить расписание напишите "добавить"',
                     reply_markup=markup_main_menu)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'расписание':
        markup = types.ReplyKeyboardMarkup(True)
        markup.row('Понедельник', 'Вторник', 'Среда')
        markup.row('Четверг', 'Пятница', 'Суббота')
        bot.send_message(message.from_user.id, 'Выберите день недели:', reply_markup=markup)
    elif message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет!')
    elif message.text.lower() == 'добавить':
        bot.send_message(message.from_user.id, 'Команда пока не реализована!')
    elif message.text.lower().strip() in days:
        bot.send_message(message.from_user.id, days[message.text.lower().strip()], reply_markup=markup_main_menu)
    else:
        bot.send_message(message.from_user.id, 'Не понимаю, что это значит.')


bot.polling(none_stop=True)
