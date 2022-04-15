import orjson
import httpx
from typing import Optional

from frontend.schemas import Task, Estimate


class TaskClient:
    def __init__(self, url: str):
        self.url = f'{url}/plannings'
        self.headers = {'Content-Type': 'application/json'}

    def get_all_tasks(self, planning_id: int) -> list[Task]:
        res = httpx.get(f'{self.url}/{planning_id}/tasks/')
        res.raise_for_status()

        tasks = res.json()
        return [Task(**task)for task in tasks]

    def add_task(self, name: str, planning_id: int) -> Task:
        url = f'{self.url}/{planning_id}/tasks/'
        new_task = Task(uid=-1, name=name)
        payload = orjson.dumps(new_task.dict())

        res = httpx.post(
            url,
            content=payload,
            headers=self.headers,
            timeout=20,
        )
        res.raise_for_status()

        task = res.json()
        return Task(**task)

    def set_score(self, planning_id: int, task_id: int, storypoint: int) -> Task:
        url = f'{self.url}/{planning_id}/tasks/{task_id}'
        payload = orjson.dumps({'score': storypoint})

        res = httpx.patch(
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

    def set_estimates(
        self,
        planning_id: int,
        task_id: int,
        user_id: int,
        storypoint: int = None,
    ) -> Optional[Estimate]:
        url = f'{self.url}/{planning_id}/tasks/{task_id}/estimates/'
        new_estimate = Estimate(uid=-1, storypoint=storypoint, user_id=user_id)
        payload = orjson.dumps(new_estimate.dict())
        res = httpx.post(
            url,
            content=payload,
            headers=self.headers,
            timeout=20,
        )
        if res.status_code == 409:
            return None

        res.raise_for_status()

        estimate = res.json()
        return Estimate(**estimate)
