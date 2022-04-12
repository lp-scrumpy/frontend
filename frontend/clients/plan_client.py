import orjson
from datetime import datetime
import httpx

from frontend.schemas import Plan


class PlanningClient:
    def __init__(self, url: str):
        self.url = f'{url}/plannings/'

    def get_by_id(self, planning_id: int) -> Plan:
        res = httpx.get(f'{self.url}{planning_id}')
        res.raise_for_status()
        plan = Plan(res.json())
        return plan

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
