import httpx

from frontend.schemas import User


class UserClient:
    def __init__(self, url: str):
        self.url = f'{url}/users'

    def get_all(self) -> list[User]:
        res = httpx.get(f'{self.url}/')
        users = res.json()
        return [User(**user)for user in users]
