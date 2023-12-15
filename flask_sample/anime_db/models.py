from datetime import datetime
from common.utils import JsonSerializable

# psk 12/13/2023
class anime(JsonSerializable):
    def __init__(
        self,
        anime_id: int,
        title: str, 
        alternative_titles: str, 
        ranking: str,
        episodes: str, 
        genres: str, 
        status: str, 
        anime_type: str, 
        created: datetime = None, 
        modified: datetime = None
        ):
        self.anime_id = anime_id
        self.title = title
        self.alternative_titles = alternative_titles
        self.ranking = ranking
        self.status = status
        self.episodes = episodes
        self.genres = genres
        self.anime_type = anime_type
        self.created = created
        self.modified = modified
