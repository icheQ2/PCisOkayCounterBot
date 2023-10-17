import telebot
import util.properties_reader as props
import service.bot_service as service

bot = telebot.TeleBot(props.get_token())

_DISPLAY_BUTTON_TEXT = "🤯 Чекнуть, сколько сейчас без поломок 🤯"
_RESET_BUTTON_TEXT = "💀 Сброс отсчёта, комп сломался 💀"
display_button = telebot.types.KeyboardButton(_DISPLAY_BUTTON_TEXT)
reset_button = telebot.types.KeyboardButton(_RESET_BUTTON_TEXT)
user_markup = telebot.types.ReplyKeyboardMarkup()
user_markup.add(display_button)
admin_markup = telebot.types.ReplyKeyboardMarkup()
admin_markup.add(display_button)
admin_markup.add(reset_button)


def choose_markup(user_id):
    if user_id in props.get_admins():
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
    if message.text == _DISPLAY_BUTTON_TEXT:
        bot.send_message(message.chat.id, service.display_runtime_text(), reply_markup=choose_markup(user_id))
        bot.register_next_step_handler(message, on_click)
    elif message.text == _RESET_BUTTON_TEXT:
        bot.send_message(message.chat.id, service.display_runtime_text(), reply_markup=choose_markup(user_id))
        bot.send_message(message.chat.id, service.display_broken_text(), reply_markup=choose_markup(user_id))
        bot.register_next_step_handler(message, on_click)


bot.polling(none_stop=True)
