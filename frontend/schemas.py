from datetime import datetime
from pydantic import BaseModel


class User(BaseModel):
    uid: int
    name: str


class Plan(BaseModel):
    uid: int
    name: str
    date: datetime


class Task(BaseModel):
    uid: int
    name: str
