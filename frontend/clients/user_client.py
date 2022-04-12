import httpx
import orjson

from frontend.schemas import User


class UserClient:
    def __init__(self, url: str):
        self.url = f'{url}/plannings'
        self.headers = {'Content-Type': 'application/json'}

    def get_all_users(self, planning_id: int) -> list[User]:
        res = httpx.get(f'{self.url}/{planning_id}/users/')
        res.raise_for_status()

        users = res.json()
        return [User(**user) for user in users]

    def add_user(self, name: str, planning_id: int) -> User:
        url = f'{self.url}/{planning_id}/users/'
        user = User(uid=-1, name=name)
        payload = orjson.dumps(user.dict())

        res = httpx.post(url, content=payload, headers=self.headers)
        res.raise_for_status()

        user = res.json()
        return User(**user)
