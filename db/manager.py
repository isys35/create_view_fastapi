import schemas
from sqlalchemy.orm import Session
from db import models
from pyteledantic import models as telegram_api_schema


def create_state(db: Session, state: schemas.State):
    db_view = models.View(text=state.view.text)
    db_state = models.State(view=db_view, input_id=state.input.id)
    db.add(db_view)
    db.add(db_state)
    db.commit()
    db.refresh(db_state)
    return db_state


def create_bot(db: Session,
               tg_user: telegram_api_schema.User,
               bot: schemas.BotBase):
    db_bot = db.query(models.Bot).filter_by(token=bot.token).first()
    if db_bot:
        return db_bot
    db_bot = models.Bot(token=bot.token)
    db_tg_user = db.query(models.TelegramUser).filter_by(id=tg_user.id).first()
    if not db_tg_user:
        db_tg_user = models.TelegramUser(**tg_user.dict())
    db_tg_user.bot = db_bot
    db.add(db_bot)
    db.add(db_tg_user)
    db.commit()
    db.refresh(db_bot)
    return db_bot


def get_bots(db: Session):
    return db.query(models.Bot).all()


def get_input_types(db: Session):
    return db.query(models.InputTypes).all()


def create_text_input(db: Session, text_input: schemas.TextBase):
    db_text_input = models.Text(value=text_input.value)
    db.add(db_text_input)
    db.commit()
    return db_text_input


def get_text_inputs(db: Session):
    return db.query(models.Text).all()