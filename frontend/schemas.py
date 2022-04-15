from datetime import datetime
from pydantic import BaseModel
from typing import Optional


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
    score: Optional[int]


class Estimate(BaseModel):
    uid: int
    user_id: int
    storypoint: Optional[int]
