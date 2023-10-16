import util.string_process as string_process


def main_menu():
    print()
    print("Выберите пункт меню:")
    print("1 - показать текущее время работы компьютера шефа")
    print("2 - компьютер шефа сломался")
    return int(input())


def display_runtime(origin_type, seconds=0, minutes=0, hours=0, days=0, years=0):
    print()
    text = "Компьютер шефа проработал аж"
    seconds_text = string_process.get_text('s', seconds)
    minutes_text = string_process.get_text('m', minutes)
    hours_text = string_process.get_text('h', hours)
    days_text = string_process.get_text('d', days)
    years_text = string_process.get_text('y', years)

    if origin_type == 's':
        text += f" {seconds_text}!"
    elif origin_type == 'm':
        text += f" {minutes_text} {seconds_text}!"
    elif origin_type == 'h':
        text += f" {hours_text} {minutes_text} {seconds_text}!"
    elif origin_type == 'd':
        text += f" {days_text} {hours_text} {minutes_text} {seconds_text}!"
    elif origin_type == 'y':
        text += f" {years_text} {days_text} {hours_text} {minutes_text} {seconds_text}!"
    elif origin_type == 'e':
        text = f"Костян, помоги!\nНачинаем с нуля.\n{text} 0 секунд!"
    else:
        print(origin_type)
        display_error("time_display")
        return

    print(text)


def display_error(error_type):
    if error_type == "menu_input":
        print("НЕВЕРНЫЙ ПУНКТ МЕНЮ!")
    elif error_type == "time_display":
        print("ОШИБКА ВЫВОДА ВРЕМЕНИ!")
