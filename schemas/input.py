
from typing import Optional
from pydantic import BaseModel


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
    type: 'InputType'
    callback: Optional['Callback']
    location: Optional['Location']
    phone: Optional['Phone']
    text: Optional['Text']

    class Config:
        orm_mode = True


from .input_type import InputType
from .callback import Callback
from .location import Location
from .phone import Phone
from .text import Text
Input.update_forward_refs()
