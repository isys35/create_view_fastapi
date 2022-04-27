from pyteledantic.models import Update
from decimal import Decimal
from sqlalchemy.orm import Session

from bot.update_handler import UpdateHandler
from db.manager import get_location, get_text

def test_set_user(update: Update):
    handler = UpdateHandler(update)
    handler.set_user()
    assert 1040023542 == handler.user.id


def test_get_input_type_value_text(update: Update):
    handler = UpdateHandler(update)
    assert 'text' == handler._get_input_type_value()


def test_get_input_type_value_location(update_location: Update):
    handler = UpdateHandler(update_location)
    assert 'location' == handler._get_input_type_value()


def test_set_location(update_location: Update, session: Session):
    handler = UpdateHandler(update_location)
    with session() as db:
        handler._set_location(db)

    assert handler._location.latitude == Decimal("53.917409")
    assert handler._location.longitude == Decimal("27.587606")

    with session() as db:
        location_db = get_location(db, handler._location.id)

    assert handler._location.id == location_db.id
    assert handler._location.latitude == location_db.latitude
    assert handler._location.longitude == location_db.longitude


def test_set_text(update: Update, session: Session):
    handler = UpdateHandler(update)
    with session() as db:
        handler._set_text(db)

    assert handler._text.value == '/start'

    with session() as db:
        text_db = get_text(db, handler._text.id)

    assert handler._text.id == text_db.id
    assert handler._text.value == text_db.value
