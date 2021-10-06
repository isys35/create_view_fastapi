from sqlalchemy import Column, String, Integer
from sqlalchemy.dialects.postgresql import VARCHAR, DOUBLE_PRECISION

from sqlalchemy.ext.declarative import declarative_base
from db import Session

from db import engine

Base = declarative_base()


class BotCommand(Base):
    __tablename__ = 'bot_command'

    id = Column(Integer, primary_key=True)
    value = Column(String(100), unique=True)


bot_command = BotCommand(value='/start')
with Session() as session:
    session.add(bot_command)
    session.commit()
