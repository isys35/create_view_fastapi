from typing import List

from fastapi import FastAPI, Depends

from db import manager
from db.core import Session
import schemas

app = FastAPI()


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()


@app.get("/commands/", response_model=List[schemas.BotCommand])
def commands(db: Session = Depends(get_db)):
    commands = manager.get_commands(db)
    return commands
