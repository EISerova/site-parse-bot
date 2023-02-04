import logging

from environs import Env, EnvError

env = Env()
env.read_env()

try:
    TOKEN = env.str("TOKEN")
    LOGIN = env.str("LOGIN")
    PASSWORD = env.str("PASSWORD")
except EnvError as error:
    logging.critical("Ошибка токена бота".format(error=error), exc_info=True)
    exit(1)

EMAIL_1 = env.str("EMAIL_1")
EMAIL_2 = env.str("EMAIL_2")
EMAIL_3 = env.str("EMAIL_3")
EMAIL_4 = env.str("EMAIL_4")
EMAIL_5 = env.str("EMAIL_5")
EMAIL_6 = env.str("EMAIL_6")
EMAIL_7 = env.str("EMAIL_7")

GAPON_EMAILS = [
    EMAIL_1,
    EMAIL_2,
    EMAIL_3,
    EMAIL_4,
    EMAIL_5,
    EMAIL_6,
    EMAIL_7,
]

SITE_ADDRESS = env.str("SITE_ADDRESS")
COMMENTS_ADDRESS = env.str("COMMENTS_ADDRESS")
LOGIN_ADDRESS = env.str("LOGIN_ADDRESS")
