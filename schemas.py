from pydantic import BaseModel

from telegram_api.models import User


class BotCommand(BaseModel):
    id: int = None
    value: str

    class Config:
        orm_mode = True


class Input(BaseModel):
    id: int

    class Config:
        orm_mode = True


class ReplyButton(BaseModel):
    id: int = None
    value: str

    class Config:
        orm_mode = True


class View(BaseModel):
    id: int
    text: str

    class Config:
        orm_mode = True


class State(BaseModel):
    id: int
    parent_id: int = None
    view: View
    input: Input

    class Config:
        orm_mode = True


class Bot(BaseModel):
    id: int
    token: str

    class Config:
        orm_mode = True


class TelegramUser(User):
    bot: Bot

    class Config:
        orm_mode = True
