from typing import List, Optional

import uvicorn

from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from db import manager
from db.core import Session

import schemas

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


@app.get("/commands/", response_model=List[schemas.BotCommand])
def get_commands(db: Session = Depends(get_db)):
    commands = manager.get_commands(db)
    return commands


@app.post("/commands/", response_model=schemas.BotCommand)
def create_command(command: schemas.BotCommand, db: Session = Depends(get_db)):
    db_command = manager.get_command_by_value(db, value=command.value)
    if db_command:
        raise HTTPException(status_code=400, detail="Комманда уже есть в базе")
    db_command = manager.create_command(db, command)
    return db_command


@app.get("/commands/{command_id}", response_model=schemas.BotCommand)
def get_command(command_id: int, db: Session = Depends(get_db)):
    db_command = manager.get_command_by_id(db, command_id=command_id)
    if not db_command:
        raise HTTPException(status_code=400, detail="Коммманда не найдена")
    return db_command


@app.delete("/commands/{command_id}")
def delete_command(command_id: int, db: Session = Depends(get_db)):
    db_command = manager.get_command_by_id(db, command_id=command_id)
    if not db_command:
        raise HTTPException(status_code=400, detail="Комманда не найдена")
    manager.delete_command(db, command_id=command_id)
    return {'status': True}


@app.patch("/commands/{command_id}")
def update_command(command_id: int, command: schemas.BotCommand, db: Session = Depends(get_db)):
    db_command = manager.get_command_by_id(db, command_id=command_id)
    if not db_command:
        raise HTTPException(status_code=400, detail="Комманда не найдена")
    manager.update_command(db, command_id=command_id, command=command)
    return {'status': True}


@app.post("/replybuttons/", response_model=schemas.ReplyButton)
def create_replybutton(reply_button: schemas.ReplyButton, db: Session = Depends(get_db)):
    db_reply_button = manager.get_reply_button_by_value(db, value=reply_button.value)
    if db_reply_button:
        raise HTTPException(status_code=400, detail="Кнопка уже есть в базе")
    db_reply_button = manager.create_reply_button(db, reply_button)
    return db_reply_button


@app.get("/replybuttons/", response_model=List[schemas.ReplyButton])
def get_replybuttons(db: Session = Depends(get_db)):
    replybuttons = manager.get_reply_buttons(db)
    return replybuttons


@app.get("/replybuttons/{replybutton_id}", response_model=schemas.ReplyButton)
def get_replybutton(replybutton_id: int, db: Session = Depends(get_db)):
    db_reply_button = manager.get_reply_button_by_id(db, replybutton_id=replybutton_id)
    if not db_reply_button:
        raise HTTPException(status_code=400, detail="Кнопка не найдена")
    return db_reply_button


@app.delete("/replybuttons/{replybutton_id}")
def delete_command(replybutton_id: int, db: Session = Depends(get_db)):
    db_reply_button = manager.get_reply_button_by_id(db, replybutton_id=replybutton_id)
    if not db_reply_button:
        raise HTTPException(status_code=400, detail="Кнопка не найдена")
    manager.delete_reply_button(db, replybutton_id=replybutton_id)
    return {'status': True}


@app.patch("/replybuttons/{replybutton_id}")
def update_reply_button(replybutton_id: int, replybutton: schemas.ReplyButton, db: Session = Depends(get_db)):
    db_reply_button = manager.get_reply_button_by_id(db, replybutton_id=replybutton_id)
    if not db_reply_button:
        raise HTTPException(status_code=400, detail="Кнопка не найдена")
    manager.update_reply_button(db, replybutton_id=replybutton_id, replybutton=replybutton)
    return {'status': True}


@app.get("/inputs/", response_model=schemas.Input)
def get_input(type: Optional[str], command_id: Optional[int], db: Session = Depends(get_db)):
    db_input = manager.get_input(db, type=type, command_id=command_id)
    if not db_input:
        raise HTTPException(status_code=400, detail="Input не найден")
    return db_input


@app.post("/states/", response_model=schemas.State)
def create_state(state: schemas.State, db: Session = Depends(get_db)):
    db_state = manager.create_state(db, state)
    return db_state


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
