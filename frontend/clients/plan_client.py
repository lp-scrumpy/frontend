import orjson
from datetime import datetime
import httpx

from frontend.schemas import Plan, Task


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
            timeout=15,
        )
        res.raise_for_status()
        plan = res.json()
        return Plan(**plan)

    def get_tasks(self, plan_id: int) -> list[Task]:
        return []
