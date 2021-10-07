from db.core import Session
from db import models


def get_commands(db: Session):
    return db.query(models.BotCommand).all()
