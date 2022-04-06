from typing import Optional, List

from pydantic import BaseModel

from pyteledantic.models import User


class View(BaseModel):
    id: int
    text: str

    class Config:
        orm_mode = True


# class StateBase(BaseModel):
#     parent_id: Optional[int] = None
#     view: View
#     input: Input


# class State(StateBase):
#     id: int

#     class Config:
#         orm_mode = True


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

class InputTypeRelated(InputType):
    inputs: List['Input']


class TextBase(BaseModel):
    value: str


class Text(TextBase):
    id: int
    

    class Config:
        orm_mode = True


class TextRelated(Text):
    inputs: List['Input']



class Callback(BaseModel):
    id: int
    
    class Config:
        orm_mode = True


class CallbackRelated(Callback):
    inputs: List['Input']


class LocationBase(BaseModel):
    longitude: float
    latitude: float


class Location(LocationBase):
    id: int

    class Config:
        orm_mode = True


class LocationRelated(Location):
    inputs: List['Input']



# TODO: вместо value лучше number, нужно менять и в бд
class PhoneBase(BaseModel):
    value: str


class Phone(PhoneBase):
    id: int

    class Config:
        orm_mode = True


class PhoneRelated(Phone):
    inputs: List['Input']



class InputBase(BaseModel):
    pass


class InputCreate(InputBase):
    type_id: int
    callback_id: Optional[int]
    location_id: Optional[int]
    phone_id: Optional[int]
    text_id: Optional[int]


class Input(InputBase):
    id: int
    type: InputType
    callback: Optional[Callback]
    location: Optional[Location]
    phone: Optional[Phone]
    text: Optional[Text]

    class Config:
        orm_mode = True




InputTypeRelated.update_forward_refs()
PhoneRelated.update_forward_refs()
LocationRelated.update_forward_refs()
CallbackRelated.update_forward_refs()
TextRelated.update_forward_refs()