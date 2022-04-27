

from typing import Optional, Union

from db.models.models import Input, InputTypes, State


class User:

    def __init__(self, user_id: Union[str, int]):
        self._id = user_id

    @property
    def id(self):
        return self._id