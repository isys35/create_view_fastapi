from typing import List

import uvicorn

from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pyteledantic.exceptions.exceptions import TelegramAPIException
from requests.exceptions import ProxyError

from db import manager
from db.core import Session

import schemas

from telegram_api import bot as tg_bot

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()


@app.get("/input-types/", response_model=List[schemas.InputTypeRelated])
def get_input_types(db: Session = Depends(get_db)):
    db_input_type = manager.get_input_types(db)
    return db_input_type


@app.post("/texts/", response_model=schemas.Text)
def create_text_inputs(text_input: schemas.TextBase, db: Session = Depends(get_db)):
    db_text_input = manager.create_text_input(db, text_input)
    return db_text_input

@app.get("/texts/", response_model=List[schemas.Text])
def get_text_inputs(db: Session = Depends(get_db)):
    db_text_inputs = manager.get_text_inputs(db)
    return db_text_inputs


@app.post("/bots/", response_model=schemas.Bot,
          responses={400: {"model": schemas.BotBase},
                     500: {"model": schemas.BotBase}})
async def create_bot(bot: schemas.BotBase, db: Session = Depends(get_db)):
    try:
        tg_user = tg_bot.Bot(bot.token).get_me()
    except TelegramAPIException as ex:
        raise HTTPException(status_code=400, detail=f"TelegramAPIError {ex.txt}")
    except ProxyError:
        raise HTTPException(status_code=500, detail=f"ProxyError")
    bot = manager.create_bot(db, tg_user, bot)
    return bot


@app.get("/bots/", response_model=List[schemas.Bot])
async def get_bots(db: Session = Depends(get_db)):
    db_bots = manager.get_bots(db)
    return db_bots


# @app.post("/states/", response_model=schemas.State)
# async def create_state(state: schemas.StateBase, db: Session = Depends(get_db)):
#     db_state = manager.create_state(db, state)
#     return db_state


@app.post("/inputs/", response_model=schemas.Input)
async def create_input(input: schemas.InputCreate, db: Session = Depends(get_db)):
    input_db = manager.create_input(db, input)
    return input_db


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
