from sqlalchemy import Column, String, Integer, Text, ForeignKey, Numeric, Table, Boolean

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

association_table = Table('reply_button_has_view', Base.metadata,
                          Column('replybutton_id', ForeignKey('replybutton.id'), primary_key=True),
                          Column('view_id', ForeignKey('view.id'), primary_key=True)
                          )


class Command(Base):
    __tablename__ = 'command'

    id = Column(Integer, primary_key=True, autoincrement=True)
    value = Column(String(100), unique=True)
    inputs = relationship("Input", back_populates="command")


class ReplyButton(Base):
    __tablename__ = 'replybutton'

    id = Column(Integer, primary_key=True, autoincrement=True)
    value = Column(String(100), unique=True)
    inputs = relationship("Input", back_populates="replybutton")
    views = relationship("View", secondary=association_table, back_populates="replybuttons")


class CallBack(Base):
    __tablename__ = 'callback'

    id = Column(Integer, primary_key=True, autoincrement=True)
    func_name = Column(String(100), unique=True)
    inputs = relationship("Input", back_populates="callback")


class Location(Base):
    __tablename__ = 'location'

    id = Column(Integer, primary_key=True, autoincrement=True)
    longitude = Column(Numeric, nullable=False)
    latitude = Column(Numeric, nullable=False)
    inputs = relationship("Input", back_populates="location")


class Input(Base):
    __tablename__ = 'input'

    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String(100), nullable=True)
    replybutton_id = Column(Integer, ForeignKey('replybutton.id'), nullable=True)
    replybutton = relationship("ReplyButton", back_populates="inputs")
    callback_id = Column(Integer, ForeignKey('callback.id'), nullable=True)
    callback = relationship("CallBack", back_populates="inputs")
    location_id = Column(Integer, ForeignKey('location.id'), nullable=True)
    location = relationship("Location", back_populates="inputs")
    phone = Column(String(100), nullable=True)
    text = Column(Text, nullable=True)
    command_id = Column(Integer, ForeignKey('command.id'), nullable=True)
    command = relationship("Command", back_populates="inputs")
    states = relationship("State", back_populates="input")


class State(Base):
    __tablename__ = 'state'

    id = Column(Integer, primary_key=True, autoincrement=True)
    parent_id = Column(Integer, ForeignKey('state.id'), nullable=True)
    parent = relationship('State', remote_side=[id])
    view_id = Column(Integer, ForeignKey('view.id'), nullable=True)
    view = relationship("View", back_populates="states")
    input_id = Column(Integer, ForeignKey('input.id'), nullable=True)
    input = relationship("Input", back_populates="states")


class View(Base):
    __tablename__ = 'view'

    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(Text)
    states = relationship("State", back_populates="view")
    replybuttons = relationship("ReplyButton", secondary=association_table, back_populates="views")


class Bot(Base):
    __tablename__ = 'bot'

    id = Column(Integer, primary_key=True, autoincrement=True)
    token = Column(Text)
    telegram_user = relationship("TelegramUser", back_populates="bot", uselist=False)


class TelegramUser(Base):
    __tablename__ = 'telegram_user'

    id = Column(Integer, primary_key=True)
    is_bot = Column(Boolean)
    first_name = Column(String(100))
    last_name = Column(String(100), nullable=True)
    user_name = Column(String(100), nullable=True)
    language_code = Column(String(100), nullable=True)
    can_join_groups = Column(Boolean, nullable=True)
    can_read_all_group_messages = Column(Boolean, nullable=True)
    supports_inline_queries = Column(Boolean, nullable=True)
    bot_id = Column(Integer, ForeignKey('bot.id'), nullable=True)
    bot = relationship("Bot", back_populates="tg_user")