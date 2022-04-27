from contextlib import contextmanager
import json

import pytest

from fastapi.testclient import TestClient

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from app import app, get_db

from db.models import Base

from pyteledantic.models import Update


SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)


@contextmanager
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db


def load_mock(mock_name: str):
    with open(f'tests/mocks/{mock_name}') as mock_file:
        data = json.load(mock_file)
        return data

@pytest.fixture
def session():
    return override_get_db

@pytest.fixture
def update():
    mock = load_mock('start_message.json')
    return Update(**mock)


@pytest.fixture
def update_location():
    mock = load_mock('location.json')
    return Update(**mock)



@pytest.fixture
def client():
    return TestClient(app)
