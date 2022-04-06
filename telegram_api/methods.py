import requests

import schemas
from telegram_api.exceptions.exceptions import TelegramAPIException
from telegram_api.models import User


def get_me(bot: schemas.Bot) -> User:
    response = requests.get(f'https://api.telegram.org/bot{bot.token}/getMe', verify=False)
    if response.status_code == 200:
        user = User(**response.json()['result'])
        return user
    else:
        description = response.json()['description']
        raise TelegramAPIException(description)
