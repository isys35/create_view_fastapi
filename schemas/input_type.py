from typing import List
from pydantic import BaseModel


class InputTypeBase(BaseModel):
    value: str


class InputType(InputTypeBase):
    id: int

    class Config:
        orm_mode = True

class InputTypeRelated(InputType):
    inputs: List['Input']

from .input import Input
InputTypeRelated.update_forward_refs()