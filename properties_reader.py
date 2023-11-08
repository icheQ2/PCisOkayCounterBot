import configparser

config = configparser.RawConfigParser()
config.read("resources/bot.properties")


def get_token():
    return config.get("DEFAULT", "token")


def get_admins():
    return config.get("DEFAULT", "admins").split()
