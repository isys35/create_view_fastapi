from pyteledantic.methods import get_me
from pyteledantic.models import Bot as BotModel, User


class Bot:
    def __init__(self, token: str):
        self.bot_model = BotModel(token=token)

    def get_me(self) -> User:
        return get_me(self.bot_model)