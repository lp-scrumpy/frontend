import orjson
import httpx

from frontend.schemas import Plan, Task


class TaskClient:
    def __init__(self, url: str):
        self.url = f'{url}/plannings/'

    def get_all_tasks(self, planning_id: int) -> list[Task]:
        res = httpx.get(f'{self.url}{planning_id}/tasks/')
        res.raise_for_status()
        tasks = res.json()
        return [Task(**task)for task in tasks]

    def add_task(self, name: str) -> Plan:
        task = Plan(uid=-1, name=name)
        payload = orjson.dumps(task.dict())
        res = httpx.post(f'{self.url}new-task', content=payload)
        res.raise_for_status()
        task = res.json()
        return Task(**task)
