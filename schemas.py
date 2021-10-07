from pydantic import BaseModel


class BotCommand(BaseModel):
    value: str

    class Config:
        orm_mod = True