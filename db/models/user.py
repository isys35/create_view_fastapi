from sqlalchemy import Column, String, Integer, Text, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from .base import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    telegram_user_id = Column(Integer, ForeignKey('telegram_user.id'))
    telegram_user = relationship("TelegramUser", back_populates="user")
    state_id = Column(Integer, ForeignKey('state.id'), nullable=True)
    state = relationship("State", back_populates="users")
