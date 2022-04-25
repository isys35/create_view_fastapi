from pyteledantic.methods import get_me, set_webhook
from pyteledantic.models import Bot as BotModel, User
from settings import HOST


class Bot:
    def __init__(self, token: str):
        self.bot_model = BotModel(token=token)

    def get_me(self) -> User:
        return get_me(self.bot_model)

    def set_webhook(self) -> bool:
        """Ссылка на webhook формируется по правилу host + bots/webhook/ + token"""
        url = HOST + f'bots/webhook/{self.bot_model.token}'
        return set_webhook(self.bot_model, url)