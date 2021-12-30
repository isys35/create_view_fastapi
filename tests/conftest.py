import pytest

from fastapi.testclient import TestClient
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from app import app, get_db

from db import manager as db_manager
from db.core import Session
from db.models import Base
from db.models import Command as CommandDB
from db.models import ReplyButton as ReplyButtonDB

from schemas import BotCommand, ReplyButton

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture
def session():
    return next(override_get_db())


@pytest.fixture
def setup(session):
    cmd = db_manager.create_command(session, BotCommand(value='test_command'))
    replybutton = db_manager.create_reply_button(session, ReplyButton(value='test_replybutton'))
    yield cmd, replybutton
    session.execute(text(f"DELETE FROM {CommandDB.__tablename__};"))
    session.execute(text(f"DELETE FROM {ReplyButtonDB.__tablename__};"))
    session.commit()


@pytest.fixture
def client():
    return TestClient(app)
