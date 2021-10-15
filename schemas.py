from pydantic import BaseModel


class BotCommand(BaseModel):
    id: int = None
    value: str

    class Config:
        orm_mode = True


class ReplyButton(BaseModel):
    id: int = None
    value: str

    class Config:
        orm_mode = True