from typing import List

import uvicorn
from fastapi import FastAPI, Depends, HTTPException

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
def get_commands(db: Session = Depends(get_db)):
    commands = manager.get_commands(db)
    return commands


@app.post("/commands/", response_model=schemas.BotCommand)
def create_command(command: schemas.BotCommand, db: Session = Depends(get_db)):
    db_command = manager.get_command(db, value=command.value)
    if db_command:
        raise HTTPException(status_code=400, detail="Данная комманда уже есть")
    db_command = manager.create_command(db, command)
    return db_command


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)