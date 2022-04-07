from typing import List
from pydantic import BaseModel


class Callback(BaseModel):
    id: int
    
    class Config:
        orm_mode = True


class CallbackRelated(Callback):
    inputs: List['Input']


from .input import Input
CallbackRelated.update_forward_refs()