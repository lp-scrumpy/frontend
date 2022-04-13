import orjson
import httpx

from frontend.schemas import Plan, Task


class TaskClient:
    def __init__(self, url: str):
        self.url = f'{url}/plannings'
        self.headers = {'Content-Type': 'application/json'}

    def get_all_tasks(self, planning_id: int) -> list[Task]:
        res = httpx.get(f'{self.url}/{planning_id}/tasks/')
        res.raise_for_status()

        tasks = res.json()
        return [Task(**task)for task in tasks]

    def add_task(self, name: str, planning_id: int) -> Plan:
        url = f'{self.url}/{planning_id}/tasks/'
        task = Task(uid=-1, name=name)
        payload = orjson.dumps(task.dict())

        res = httpx.post(
            url,
            content=payload,
            headers=self.headers,
            timeout=20,
        )
        res.raise_for_status()

        task = res.json()
        return Task(**task)

    def get_by_id(self, task_id: int, planning_id: int) -> Task:
        url = f'{self.url}/{planning_id}/tasks/{task_id}'
        res = httpx.get(url)
        res.raise_for_status()

        task = res.json()
        return Task(**task)
