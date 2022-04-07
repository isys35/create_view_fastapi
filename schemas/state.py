from typing import Optional
from pydantic import BaseModel


class StateBase(BaseModel):
    parent_id: Optional[int] = None
    view_id: int
    input_id: int


class State(StateBase):
    id: int
    parent: Optional['State'] = None
    view: 'View'
    input: 'Input'

    class Config:
        orm_mode = True


from .input import Input
from .view import View
State.update_forward_refs()