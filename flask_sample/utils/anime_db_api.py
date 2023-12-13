from utils.api import API
class Anime:
    @staticmethod
    def get_anime(page = 1, page_size = 10):
        # Build query based on parameters and Anime DB API specifications
        query = {"page":page, "pageSize": page_size}
        results = API.get("/anime",query, "H_API")
        print(f"API Results: {results}")
       
if __name__ == "__main__":
    Anime.get_anime(1,1)