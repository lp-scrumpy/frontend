import orjson
from datetime import datetime
import httpx

from frontend.schemas import Plan, User


class PlanningClient:
    def __init__(self, url: str):
        self.url = f'{url}/plannings/'

    def get_all(self) -> list[Plan]:
        res = httpx.get(self.url)
        res.raise_for_status()
        plans = res.json()
        return [Plan(**plan)for plan in plans]

    def add(self, name: str, date: datetime) -> Plan:
        plan = Plan(uid=-1, name=name, date=date)
        payload = orjson.dumps(plan.dict())
        res = httpx.post(
            self.url,
            content=payload,
            headers={'Content-Type': 'application/json'},
            timeout=20,
        )
        res.raise_for_status()
        plan = res.json()
        return Plan(**plan)

    def get_all_users(self) -> list[User]:
        res = httpx.get(f'{self.url}')
        res.raise_for_status()
        users = res.json()
        return [User(**user)for user in users]

    def add_user(self, name: str) -> User:
        user = User(uid=-1, name=name)
        payload = orjson.dumps(user.dict())
        res = httpx.post(f'{self.url}new-user', content=payload)
        res.raise_for_status()
        user = res.json()
        return User(**user)
