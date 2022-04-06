from typing import Optional

import schemas
from sqlalchemy.orm import Session
from db import models
from telegram_api import models as telegram_api_schema


def get_commands(db: Session):
    return db.query(models.Command).all()


def create_command(db: Session, command: schemas.BotCommand):
    db_command = models.Command(value=command.value)
    db_input = models.Input(command=db_command, text=command.value, type='command')
    db.add(db_input)
    db.add(db_command)
    db.commit()
    db.refresh(db_command)
    return db_command


def get_command_by_value(db: Session, value: str):
    return db.query(models.Command).filter(models.Command.value == value).first()


def get_command_by_id(db: Session, command_id: int):
    return db.query(models.Command).filter(models.Command.id == command_id).first()


def delete_command(db: Session, command_id: int):
    db.query(models.Input).filter(models.Input.command_id == command_id).delete()
    db.query(models.Command).filter(models.Command.id == command_id).delete()
    db.commit()


def update_command(db: Session, command_id: int, command: schemas.BotCommand):
    db.query(models.Command).filter(models.Command.id == command_id).update({"value": command.value})
    db.commit()


def create_reply_button(db: Session, reply_button: schemas.ReplyButton):
    db_reply_button = models.ReplyButton(value=reply_button.value)
    db.add(db_reply_button)
    db.commit()
    db.refresh(db_reply_button)
    return db_reply_button


def get_reply_button_by_value(db: Session, value: str):
    return db.query(models.ReplyButton).filter(models.ReplyButton.value == value).first()


def get_reply_button_by_id(db: Session, replybutton_id: int):
    return db.query(models.ReplyButton).filter(models.ReplyButton.id == replybutton_id).first()


def get_reply_buttons(db: Session):
    return db.query(models.ReplyButton).all()


def delete_reply_button(db: Session, replybutton_id: int):
    db.query(models.ReplyButton).filter(models.ReplyButton.id == replybutton_id).delete()
    db.commit()


def update_reply_button(db: Session, replybutton_id: int, replybutton: schemas.BotCommand):
    db.query(models.ReplyButton).filter(models.ReplyButton.id == replybutton_id).update({"value": replybutton.value})
    db.commit()


def get_input(db: Session, type: Optional[str], command_id: Optional[int]):
    if type == 'command':
        return db.query(models.Input).filter(models.Input.type == type,
                                             models.Input.command_id == command_id).first()


def create_state(db: Session, state: schemas.State):
    db_view = models.View(text=state.view.text)
    db_state = models.State(view=db_view, input_id=state.input.id)
    db.add(db_view)
    db.add(db_state)
    db.commit()
    db.refresh(db_state)
    return db_state


def create_bot(db: Session, tg_user: telegram_api_schema.User, bot: schemas.Bot):
    db_bot = models.Bot(token=bot.token)
    db_tg_user = models.TelegramUser(**tg_user.dict())
    db_tg_user.bot = db_bot
    db.add(db_bot)
    db.add(db_tg_user)
    db.commit()
    db.refresh(db_bot)
    return db_bot
