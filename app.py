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


@app.post("/states/", response_model=schemas.State)
def create_state(state: schemas.State, db: Session = Depends(get_db)):
    db_state = manager.create_state(db, state)
    return db_state


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


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
