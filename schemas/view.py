
from typing import List
from pydantic import BaseModel


class ViewBase(BaseModel):
    text: str


class View(ViewBase):
    id: int

    class Config:
        orm_mode = True

class ViewRelated(View):
    states: List['State']

from .state import State
ViewRelated.update_forward_refs()