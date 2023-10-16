import time


def get_current():
    return int(time.time())


def get_seconds(origin):
    return get_current() - origin


def get_minutes(seconds):
    return int(seconds / 60)


def get_hours(seconds):
    return int(get_minutes(seconds) / 60)


def get_days(seconds):
    return int(get_hours(seconds) / 24)


def get_years(seconds):
    return int(get_days(seconds) / 365)
