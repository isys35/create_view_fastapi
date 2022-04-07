
# TODO: вместо value лучше number, нужно менять и в бд
from typing import List
from pydantic import BaseModel


class PhoneBase(BaseModel):
    value: str


class Phone(PhoneBase):
    id: int

    class Config:
        orm_mode = True


class PhoneRelated(Phone):
    inputs: List['Input']


from .input import Input
PhoneRelated.update_forward_refs()