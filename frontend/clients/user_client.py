import httpx


class UserClient:
    def __init__(self, url: str):
        self.url = f'{url}/users'

    def get_all(self):
        res = httpx.get(f'{self.url}/')
        return res.json()
