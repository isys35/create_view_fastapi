
from typing import List
from pydantic import BaseModel


class TextBase(BaseModel):
    value: str


class Text(TextBase):
    id: int
    

    class Config:
        orm_mode = True


class TextRelated(Text):
    inputs: List['Input']

from .input import Input
TextRelated.update_forward_refs()