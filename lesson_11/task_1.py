import telebot
from lesson_11 import manager_db as md

"""
Написать бота-консультанта, который будет собирать информацию с
пользователя (его ФИО, номер телефона, почта, адресс, пожелания).
Записывать сформированную заявку в БД (по желанию SQl/NOSQL).)

"""

bot = telebot.TeleBot('1110894638:AAGC1Y9zoL8FMDJsqJKAF6MMSJ5jPwQc3iU')
base = 'info_db.db'
users_dict = {}


class Users:
    def __init__(self, first_name):
        self.first_name = first_name
        self.last_name = None
        self.user_email = None
        self.user_phone = None
        self.user_address = None
        self.user_wishes = None


@bot.message_handler(commands=['start'])
def start(message):
    msg = bot.send_message(message.chat.id, 'Ведите имя')
    bot.register_next_step_handler(msg, first_name_step)


def first_name_step(message):
    user_id = message.from_user.id
    first_name = message.text
    users_dict[user_id] = Users(first_name)
    try:
        with md.BaseManager(base) as db:
            db.execute('''
                        INSERT INTO people ('telegram_id')
                        VALUES (?)
                        ''', [user_id])
            db.fetchall()
    except Exception as err:
        bot.send_message(message.chat.id, 'Произошла ошибка, Вы уже были зарегистрированны')
    else:
        msg = bot.send_message(message.chat.id, 'Введите фамилию')
        bot.register_next_step_handler(msg, last_name_step)


def last_name_step(message):
    user_id = message.from_user.id
    user = users_dict[user_id]
    user.last_name = message.text

    msg = bot.send_message(message.chat.id, 'Введите свою почту')
    bot.register_next_step_handler(msg, email_step)


def email_step(message):
    user_id = message.from_user.id
    user = users_dict[user_id]
    user.user_email = message.text

    msg = bot.send_message(message.chat.id, 'Введите свой номер телефона')
    bot.register_next_step_handler(msg, phone_step)


def phone_step(message):
    user_id = message.from_user.id
    user = users_dict[user_id]
    user.user_phone = message.text

    msg = bot.send_message(message.chat.id, 'Введите свой адрес')
    bot.register_next_step_handler(msg, address_step)


def address_step(message):
    user_id = message.from_user.id
    user = users_dict[user_id]
    user.user_address = message.text

    msg = bot.send_message(message.chat.id, 'Ваши пожелания')
    bot.register_next_step_handler(msg, wishes_step)


def wishes_step(message):
    user_id = message.from_user.id
    user = users_dict[user_id]
    user.user_wishes = message.text
    sql = 'UPDATE people SET name = ?, surname = ?, phone_number = ?, email = ?, address = ?, wishes = ? WHERE telegram_id = ?'
    with md.BaseManager(base) as db:
            db.execute(sql, [user.first_name, user.last_name, user.user_email, user.user_phone,
                             user.user_address, user.user_wishes, user_id])
            db.fetchall()
    bot.send_message(message.chat.id, 'Готово')


bot.polling()

