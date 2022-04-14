import httpx

from frontend.schemas import Estimate


class EstimateClient:
    def __init__(self, url: str):
        self.url = f'{url}/plannings'

    def get_estimates(self, planning_id: int, task_id: int) -> list[Estimate]:
        res = httpx.get(f'{self.url}/{planning_id}/tasks/{task_id}/score/')

        estimates = res.json()
        return [Estimate(**estimate)for estimate in estimates]
