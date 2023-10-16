from util.time_process import get_current

_FILE_PATH = "data/date.txt"


def rewrite_time():
    with open(_FILE_PATH, 'w') as file:
        file.write(str(get_current()))


def read_time():
    with open(_FILE_PATH, 'r') as file:
        return int(file.read())
