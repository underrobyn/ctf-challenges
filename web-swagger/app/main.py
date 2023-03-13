from typing import Union
from fastapi import FastAPI
from models import User, SessionLocal


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/users/")
def create_user(name: str, email: str, password: str):
    db = SessionLocal()
    user = User(name=name, email=email)
    user.set_password(password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
