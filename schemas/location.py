from typing import List
from pydantic import BaseModel


class LocationBase(BaseModel):
    longitude: float
    latitude: float


class Location(LocationBase):
    id: int

    class Config:
        orm_mode = True


class LocationRelated(Location):
    inputs: List['Input']


from .input import Input
LocationRelated.update_forward_refs()