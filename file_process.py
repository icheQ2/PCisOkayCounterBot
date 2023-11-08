from os import environ
from time_process import get_current

date_file_path = environ['DATE_FILE_PATH']


def rewrite_time():
    with open(date_file_path, 'w') as file:
        file.write(str(get_current()))


def read_time():
    with open(date_file_path, 'r') as file:
        return int(file.read())
