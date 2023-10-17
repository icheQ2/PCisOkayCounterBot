_WORDS = {'y': ['лет', 'год', 'года'],
          'd': ['дней', 'день', 'дня'],
          'h': ['часов', 'час', 'часа'],
          'm': ['минут', 'минуту', 'минуты'],
          's': ['секунд', 'секунду', 'секунды']}


def get_runtime_text(origin_type, seconds=0, minutes=0, hours=0, days=0, years=0):
    text = "🫡 Компьютер шефа проработал аж"
    seconds_text = get_declension_text('s', seconds)
    minutes_text = get_declension_text('m', minutes)
    hours_text = get_declension_text('h', hours)
    days_text = get_declension_text('d', days)
    years_text = get_declension_text('y', years)

    if origin_type == 's':
        text += f" {seconds_text}"
    elif origin_type == 'm':
        text += f" {minutes_text} {seconds_text}"
    elif origin_type == 'h':
        text += f" {hours_text} {minutes_text} {seconds_text}"
    elif origin_type == 'd':
        text += f" {days_text} {hours_text} {minutes_text} {seconds_text}"
    elif origin_type == 'y':
        text += f" {years_text} {days_text} {hours_text} {minutes_text} {seconds_text}"
    elif origin_type == 'e':
        text = f"🤲🏿 Костян, помоги!\n🤡 Начинаем с нуля.\n{text} 0 секунд"
    else:
        return get_error_text("time_display")

    text += "!"
    return text


def get_error_text(error_type):
    if error_type == "menu_input":
        return "НЕВЕРНЫЙ ПУНКТ МЕНЮ!"
    elif error_type == "time_display":
        return "ОШИБКА ВЫВОДА ВРЕМЕНИ!"


def get_declension_text(origin_type, number):
    remainder = number % 10

    if number == 0 or remainder == 0 or remainder >= 5 or number in range(11, 19):
        text = f"{number} {_WORDS[origin_type][0]}"
    elif remainder == 1:
        text = f"{number} {_WORDS[origin_type][1]}"
    else:
        text = f"{number} {_WORDS[origin_type][2]}"

    return text
