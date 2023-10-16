_WORDS = {'y': ['лет', 'год', 'года'],
          'd': ['дней', 'день', 'дня'],
          'h': ['часов', 'час', 'часа'],
          'm': ['минут', 'минуту', 'минуты'],
          's': ['секунд', 'секунду', 'секунды']}


def get_text(origin_type, number):
    remainder = number % 10

    if number == 0 or remainder == 0 or remainder >= 5 or number in range(11, 19):
        text = f"{number} {_WORDS[origin_type][0]}"
    elif remainder == 1:
        text = f"{number} {_WORDS[origin_type][1]}"
    else:
        text = f"{number} {_WORDS[origin_type][2]}"

    return text
