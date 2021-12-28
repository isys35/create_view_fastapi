from typing import Optional

from pydantic import BaseModel


class Bot(BaseModel):
    """
    Contains your bot token
    """
    token: str


class User(BaseModel):
    """
    https://core.telegram.org/bots/api#user
    This object represents a Telegram user or bot.
    """
    id: int
    is_bot: bool
    first_name: str
    last_name: Optional[str] = None
    username: Optional[str] = None
    language_code: Optional[str] = None
    can_join_groups: Optional[bool] = None
    can_read_all_group_messages: Optional[bool] = None
    supports_inline_queries: Optional[bool] = None
