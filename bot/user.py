

from typing import Optional, Union

from db.models.input_types import Location, Text, Phone, CallBack
from db.models.models import Input, InputTypes, State, TelegramUser


class UserBase:
    _input_type: Optional[InputTypes] = None
    _location: Optional[Location] = None
    _phone: Optional[Phone] = None
    _text: Optional[Text] = None
    _callback: Optional[CallBack] = None
    _telegram_user: Optional[TelegramUser] = None

    def __init__(self, user_id: Union[str, int]):
        self._id = user_id

    @property
    def id(self):
        return self._id

    @property
    def input_type(self):
        return self._input_type

    @property
    def location(self):
        return self._location


    @property
    def phone(self):
        return self._phone

    @property
    def text(self):
        return self._text

    
    @property
    def callback(self):
        return self._callback


    @property
    def telegram_user(self):
        return self._telegram_user

    
    @input_type.setter
    def input_type(self, input_type: InputTypes):
        self._input_type = input_type


    @location.setter
    def location(self, location: Location):
        self._location = location

    
    @phone.setter
    def phone(self, phone: Phone):
        self._phone = phone

    
    @text.setter
    def text(self, text: Text):
        self._text = text
    
    @callback.setter
    def callback(self, callback: CallBack):
        self._callback = callback


    @telegram_user.setter
    def telegram_user(self, telegram_user: TelegramUser):
        self._telegram_user = telegram_user



class User(UserBase):
    _state = Optional[State] = None

    def __init__(self, user_id: Union[str, int]):
        super().__init__(user_id)
        self.__init_from_db()

    @property
    def state(self):
        return self._state

    def __init_from_db(self):
        pass
