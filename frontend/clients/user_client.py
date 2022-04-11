import httpx
import orjson

from frontend.schemas import User


class UserClient:
    def __init__(self, url: str):
        self.url = f'{url}/plannings/'

    def get_all_users(self, planning_id: int) -> list[User]:
        res = httpx.get(f'{self.url}{planning_id}')
        res.raise_for_status()
        users = User(**res.json())
        return users


    def add_user(self, name: str) -> User:
        user = User(uid=-1, name=name)
        payload = orjson.dumps(user.dict())
        res = httpx.post(f'{self.url}new-user', content=payload)
        res.raise_for_status()
        user = res.json()
        return User(**user)
