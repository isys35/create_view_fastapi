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


def update_command(db: Session, command_id: int, command: schemas.BotCommand):
    db.query(models.BotCommand).filter(models.BotCommand.id == command_id).update({"value": command.value})
    db.commit()


def create_reply_button(db: Session, reply_button: schemas.ReplyButton):
    db_reply_button = models.ReplyButton(value=reply_button.value)
    db.add(db_reply_button)
    db.commit()
    db.refresh(db_reply_button)
    return db_reply_button


def get_reply_button_by_value(db: Session, value: str):
    return db.query(models.ReplyButton).filter(models.ReplyButton.value == value).first()
