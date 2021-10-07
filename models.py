from sqlalchemy import Column, String, Integer

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BotCommand(Base):
    __tablename__ = 'bot_command'

    id = Column(Integer, primary_key=True)
    value = Column(String(100), unique=True)