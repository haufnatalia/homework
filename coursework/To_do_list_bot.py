from telebot import TeleBot
from datetime import datetime
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = '1420592887:AAGxDsWvjC1D0L158Ycjd7UpEyx82GOX0vg'
bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def message_handler(message):
    bot.send_message(message.chat.id, 'Выбери действие:', reply_markup=gen_markup())


def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
                InlineKeyboardButton('1. Добавить новую заметку', callback_data='1'),
                InlineKeyboardButton('2. Посмотреть все заметки', callback_data='2'),
                InlineKeyboardButton('3. Удалить заметку', callback_data='3'))
    return markup


@bot.callback_query_handler(func=lambda call: True)
def iq_callback(query):
    data = query.data
    if data == '1':
        bot.answer_callback_query(query.id)
        bot.send_message(query.message.chat.id, 'Введите дату в формате дд.мм.гггг')
        bot.register_next_step_handler(query.message, check_day)
    elif data == '2':
        bot.answer_callback_query(query.id)
        with open('bot.txt', 'r') as text_notice:
            bot.send_message(query.message.chat.id, text_notice.read())
    elif data == '3':
        bot.answer_callback_query(query.id)
        bot.send_message(query.message.chat.id, 'Введите номер заметки, которую хотите удалить.')
        with open('bot.txt', 'r+') as text_notice:
            bot_text = text_notice.readlines()
            for i, x in enumerate(bot_text):
                new_bot_text = ('{0}. {1}'.format(i+1, x))
                bot.send_message(query.message.chat.id, new_bot_text)
        bot.register_next_step_handler(query.message, del_notice)


def check_day(message):
    global day
    day = message.text
    try:
        datetime.strptime(day, '%d.%m.%Y')
        with open('bot.txt', 'a+') as text_notice:
            text_notice.write(day + ' ')
            text_notice.close()
            bot.send_message(message.from_user.id, 'Введите текст')
            bot.register_next_step_handler(message, add_notice)
    except ValueError:
        bot.send_message(message.from_user.id, 'Введено не верно. Введите дату в формате дд.мм.гггг')
        bot.register_next_step_handler(message, check_day)


def add_notice(message):
    global notice
    notice = message.text
    with open('bot.txt', 'a+') as text_notice:
        text_notice.write(notice + '\n')
        text_notice.close()
    bot.send_message(message.from_user.id, 'Ваша заметка: \n\n' + day + '\n' + notice + '\n\n' + 'Сохранена.')


def del_notice(message):
    num_del = int(message.text)
    with open('bot.txt', 'r') as text_notice:
        list_n = text_notice.readlines()
    del list_n[num_del-1]
    with open('bot_new.txt', 'w+') as t_notice:
        t_notice.writelines(list_n)
    bot.send_message(message.from_user.id, 'Готово!')
    with open('bot_new.txt', 'r') as t_notice:
        t_read = t_notice.read()
    bot.send_message(message.from_user.id, t_read)


bot.polling(none_stop=True)
