from pyteledantic.models import User

class TelegramUser(User):

    class Config:
        orm_mode = True
