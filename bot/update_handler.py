from sqlalchemy.orm import Session

from typing import Optional

from pyteledantic.models import Update

from app import get_db

from bot.user import User

from db.models.input_types import Location, Text, Phone, CallBack
from db.models.models import InputTypes
from db.manager import create_location, get_input_type, create_text


class UpdateHandler:
    _user: Optional[User] = None
    _input_type: Optional[InputTypes] = None
    _location: Optional[Location] = None
    _phone: Optional[Phone] = None
    _text: Optional[Text] = None
    _phone: Optional[Phone] = None
    _callback: Optional[CallBack] = None

    def __init__(self, update: Update):
        self._update = update

    def set_user(self):
        if self._update.message:
            user_id = self._update.message.from_user.id
        else:
            user_id = self._update.callback_query.from_user.id
        self._user = User(user_id)
    
    @property
    def user(self):
        return self._user

    def _get_input_type_value(self):
        if self._update.message.location:
            return 'location'
        elif self._update.message.text:
            return 'text'
        raise Exception
    
    def _set_input_type(self):
        METHOD_SET_TYPE = {
            'location': self._set_location, 
            'text': self._set_text
        }
        input_type_value = self._get_input_type_value()
        with get_db() as db:
            self._input_type = get_input_type(db, input_type_value)
            METHOD_SET_TYPE.get(input_type_value)(db)

    
    def _set_location(self, db: Session):
        self._location = create_location(db, self._update.message.location)


    def _set_text(self, db):
        self._text = create_text(db, self._update.message.text)
