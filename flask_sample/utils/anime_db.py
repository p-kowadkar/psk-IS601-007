from api import API
class Anime:
    @staticmethod
    def get_anime(page=1, page_size=10):
        query = {"page": page, "pageSize": page_size}
        results = API.get("/anime", query, API.API_KEY, base_url=API.BASE_URL)
        return results