from sqlalchemy import Column, Integer, Numeric, Text, String
from sqlalchemy.orm import relationship

from .base import Base

# TODO: Лучше переименовать, сделать вида *Input

class CallBack(Base):
    __tablename__ = 'callback'

    id = Column(Integer, primary_key=True, autoincrement=True)
    inputs = relationship("Input", back_populates="callback")


class Location(Base):
    __tablename__ = 'location'

    id = Column(Integer, primary_key=True, autoincrement=True)
    longitude = Column(Numeric, nullable=False)
    latitude = Column(Numeric, nullable=False)
    inputs = relationship("Input", back_populates="location")


class Text(Base):
    __tablename__ = 'text'
    # TODO: Может лучше сделать value уникальным?
    id = Column(Integer, primary_key=True, autoincrement=True)
    value = Column(Text, nullable=False)
    inputs = relationship("Input", back_populates="text")


class Phone(Base):
    __tablename__ = 'phone'

    id = Column(Integer, primary_key=True, autoincrement=True)
    value = Column(String(100), nullable=False)
    inputs = relationship("Input", back_populates="phone")
