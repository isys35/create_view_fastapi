import schemas
from sqlalchemy.orm import Session
from db import models


def get_commands(db: Session):
    return db.query(models.BotCommand).all()


def create_command(db: Session, command: schemas.BotCommand):
    db_command = models.BotCommand(value=command.value)
    db.add(db_command)
    db.commit()
    return db_command
