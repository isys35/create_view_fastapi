from pydantic import BaseModel


class BotCommand(BaseModel):
    id: int = None
    value: str

    class Config:
        orm_mode = True