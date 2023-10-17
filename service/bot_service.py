import util.file_process as file_service
import util.time_process as time_service
import util.string_process as string_service


def display_runtime_text():
    diff = time_service.get_seconds(file_service.read_time())

    seconds = diff % 60
    minutes = time_service.get_minutes(diff) % 60
    hours = time_service.get_hours(diff) % 24
    days = time_service.get_days(diff) % 365
    years = time_service.get_years(diff)

    origin_type = get_origin_type(seconds, minutes, hours, days, years)
    return string_service.get_runtime_text(origin_type, seconds, minutes, hours, days, years)


def display_broken_text():
    file_service.rewrite_time()
    return string_service.get_runtime_text('e')


def get_origin_type(seconds, minutes, hours, days, years):
    if years > 0:
        return 'y'
    elif days > 0:
        return 'd'
    elif hours > 0:
        return 'h'
    elif minutes > 0:
        return 'm'
    elif seconds >= 0:
        return 's'
    else:
        return None
