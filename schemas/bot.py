from pydantic import BaseModel

from schemas.telegram_user import TelegramUser


class BotBase(BaseModel):
    token: str

class Bot(BotBase):
    id: int
    telegram_user: TelegramUser

    class Config:
        orm_mode = True