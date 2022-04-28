
from typing import Optional, Union
from app import get_db
from bot.handlers.interface import HandlerInterface
from pyteledantic.models import Update
from sqlalchemy.orm import Session
from bot.user import User
from db.manager import create_location, create_or_get_tg_user, create_text, get_input_type

class MessageHandler(HandlerInterface):

    def __init__(self, update: Update):
        self._update = update


    @property
    def input_type(self):
        if self._update.message.location:
            return 'location'
        elif self._update.message.text:
            return 'text'
        raise Exception

    @property
    def user(self):
        return self._update.message.from_user



class CallBackHandler(HandlerInterface):

    def __init__(self, update: Update):
        self._update = update
    
    @property
    def input_type(self):
        return 'callback'

    @property
    def user(self):
        return self._update.callback_query.from_user




class UpdateHandler(HandlerInterface):
    _user: Optional[User] = None
    _handler: Union[MessageHandler, CallBackHandler]

    def __init__(self, update: Update):
        self._update = update
        self.__switching_handlers()
    
    @property
    def user(self):
        return self._user

    def __switching_handlers(self):
        if self._update.message:
            self._handler = MessageHandler(self._update)
        elif self._update.callback_query:
            self._handler = CallBackHandler(self._update)

    def set_user(self):
        self._user = User(self._handler.user.id)
        with get_db() as db:
            self._set_telegram_user(db)
            self._set_user_input_type(db)
    
    def _set_telegram_user(self, db: Session):
        self.user.telegram_user = create_or_get_tg_user(db, self._handler.user)

    def _set_user_location(self, db: Session):
        self.user.location = create_location(db, self._update.message.location)

    def _set_user_text(self, db: Session):
        self.user.text = create_text(db, self._update.message.text)
    
    def _set_user_input_type(self, db):
        METHOD_SET_TYPE = {
            'location': self._set_location, 
            'text': self._set_text
        }
        self.user.input_type = get_input_type(db, self._handler.input_type)
        METHOD_SET_TYPE.get(self._handler.input_type)(db)

    