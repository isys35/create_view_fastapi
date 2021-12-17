from pydantic import BaseModel


class BotCommand(BaseModel):
    id: int = None
    value: str

    class Config:
        orm_mode = True


class Input(BaseModel):
    id: int

    class Config:
        orm_mode = True


class ReplyButton(BaseModel):
    id: int = None
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
    parent_id: int = None
    view: View
    input: Input

    class Config:
        orm_mode = True

