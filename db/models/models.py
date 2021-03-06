from sqlalchemy import Column, String, Integer, Text, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from .input_types import Base


class InputTypes(Base):
    __tablename__ = 'input_types'

    id = Column(Integer, primary_key=True, autoincrement=True)
    value = Column(String(100), nullable=False)
    inputs = relationship("Input", back_populates="type")


class Input(Base):
    __tablename__ = 'input'

    id = Column(Integer, primary_key=True, autoincrement=True)
    type_id = Column(Integer, ForeignKey('input_types.id'))
    type = relationship("InputTypes", back_populates="inputs")
    callback_id = Column(Integer, ForeignKey('callback.id'), nullable=True)
    callback = relationship("CallBack", back_populates="inputs")
    location_id = Column(Integer, ForeignKey('location.id'), nullable=True)
    location = relationship("Location", back_populates="inputs")
    phone_id = Column(Integer, ForeignKey('phone.id'), nullable=True)
    phone = relationship("Phone", back_populates="inputs")
    text_id = Column(Integer, ForeignKey('text.id'), nullable=True)
    text = relationship("Text", back_populates="inputs")
    states = relationship("State", back_populates="input")


class Script(Base):
    __tablename__ = 'script'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    description = Column(Text, nullable=True)
    states = relationship("State", back_populates="script")
    bots = relationship("Bot", back_populates="script")


class State(Base):
    __tablename__ = 'state'

    id = Column(Integer, primary_key=True, autoincrement=True)
    parent_id = Column(Integer, ForeignKey('state.id'), nullable=True)
    parent = relationship('State', remote_side=[id])
    view_id = Column(Integer, ForeignKey('view.id'), nullable=True)
    view = relationship("View", back_populates="states")
    input_id = Column(Integer, ForeignKey('input.id'), nullable=True)
    input = relationship("Input", back_populates="states")
    script_id = Column(Integer, ForeignKey('script.id'))
    script = relationship("Script", back_populates="states")
    users = relationship("Users", back_populates="state")


class View(Base):
    __tablename__ = 'view'

    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(Text)
    states = relationship("State", back_populates="view")

class Bot(Base):
    __tablename__ = 'bot'

    id = Column(Integer, primary_key=True, autoincrement=True)
    token = Column(Text, unique=True)
    telegram_user = relationship("TelegramUser", back_populates="bot", uselist=False)
    script_id = Column(Integer, ForeignKey('script.id'), nullable=True)
    script = relationship("Script", back_populates="bots")


class TelegramUser(Base):
    __tablename__ = 'telegram_user'

    id = Column(Integer, primary_key=True)
    is_bot = Column(Boolean)
    first_name = Column(String(100))
    last_name = Column(String(100), nullable=True)
    username = Column(String(100), nullable=True)
    language_code = Column(String(100), nullable=True)
    can_join_groups = Column(Boolean, nullable=True)
    can_read_all_group_messages = Column(Boolean, nullable=True)
    supports_inline_queries = Column(Boolean, nullable=True)
    bot_id = Column(Integer, ForeignKey('bot.id'), nullable=True)
    bot = relationship("Bot", back_populates="telegram_user")
    user = relationship("User", back_populates="telegram_user", uselist=False)
