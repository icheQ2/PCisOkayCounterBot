from os import environ
import bot_service as service
import telebot

bot = telebot.TeleBot(environ['BOT_TOKEN'])

_DISPLAY_BUTTON_TEXT = "🤯 Чекнуть, сколько сейчас без поломок 🤯"
_RESET_BUTTON_TEXT = "💀 Сброс отсчёта, комп сломался 💀"
display_button = telebot.types.KeyboardButton(_DISPLAY_BUTTON_TEXT)
reset_button = telebot.types.KeyboardButton(_RESET_BUTTON_TEXT)
user_markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
user_markup.add(display_button)
admin_markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
admin_markup.add(display_button)
admin_markup.add(reset_button)


def choose_markup(user_id):
    admin_ids = environ['ADMIN_IDS'].split(', ')
    if user_id in admin_ids:
        return admin_markup
    else:
        return user_markup


@bot.message_handler(commands=["start"])
def start(message):
    user_id = str(message.from_user.id)
    bot.send_message(message.chat.id,
                     f"👻 Добро пожаловать, {message.from_user.first_name} {message.from_user.last_name}!",
                     reply_markup=choose_markup(user_id))
    bot.register_next_step_handler(message, on_click)


@bot.message_handler(commands=["getid"])
def get_id(message):
    user_id = str(message.from_user.id)
    bot.send_message(message.chat.id,
                     f"😎 Ты прошёл Телеграм. Перешли Димону свой id: {user_id}",
                     reply_markup=choose_markup(user_id))
    print(message.chat.id)
    bot.register_next_step_handler(message, on_click)


def on_click(message):
    user_id = str(message.from_user.id)
    if message.text == "/start":
        start(message)
    elif message.text == "/getid":
        get_id(message)
    elif message.text == _DISPLAY_BUTTON_TEXT:
        bot.send_message(message.chat.id, service.display_runtime_text(), reply_markup=choose_markup(user_id))
        bot.register_next_step_handler(message, on_click)
    elif message.text == _RESET_BUTTON_TEXT:
        bot.send_message(message.chat.id, service.display_runtime_text(), reply_markup=choose_markup(user_id))
        bot.send_message(message.chat.id, service.display_broken_text(), reply_markup=choose_markup(user_id))
        bot.register_next_step_handler(message, on_click)


bot.polling(none_stop=True)
