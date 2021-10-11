import schemas
from sqlalchemy.orm import Session
from db import models


def get_commands(db: Session):
    return db.query(models.BotCommand).all()


def create_command(db: Session, command: schemas.BotCommand):
    db_command = models.BotCommand(value=command.value)
    db.add(db_command)
    db.commit()
    db.refresh(db_command)
    return db_command


def get_command_by_value(db: Session, value: str):
    return db.query(models.BotCommand).filter(models.BotCommand.value == value).first()


def get_command_by_id(db: Session, command_id: int):
    return db.query(models.BotCommand).filter(models.BotCommand.id == command_id).first()


def delete_command(db: Session, command_id: int):
    db.query(models.BotCommand).filter(models.BotCommand.id == command_id).delete()
    db.commit()


def update_command(db: Session, command_id: int,  command: schemas.BotCommand):
    db.query(models.BotCommand).filter(models.BotCommand.id == command_id).update({"value": command.value})
    db.commit()