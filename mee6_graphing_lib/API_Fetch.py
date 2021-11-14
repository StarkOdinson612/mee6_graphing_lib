from mee6_py_api import API


class API_Fetch_Class:
    def __init__(self):
        self.mee6API = API(377946908783673344)

    async def API_fetch(self, index):
        return await self.mee6API.levels.get_leaderboard_page(index)
