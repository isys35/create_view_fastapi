from typing import Optional

from pydantic import BaseModel

from pyteledantic.models import User


class BotCommand(BaseModel):
    id: Optional[int] = None
    value: str

    class Config:
        orm_mode = True


class Input(BaseModel):
    id: int

    class Config:
        orm_mode = True


class ReplyButton(BaseModel):
    id: Optional[int] = None
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
    parent_id: Optional[int] = None
    view: View
    input: Input

    class Config:
        orm_mode = True


class BotBase(BaseModel):
    token: str


class TelegramUser(User):

    class Config:
        orm_mode = True


class Bot(BotBase):
    id: int
    telegram_user: TelegramUser

    class Config:
        orm_mode = True


class InputTypeBase(BaseModel):
    value: str

class InputType(InputTypeBase):
    id: int

    class Config:
        orm_mode = True