
import os
# fix for testing just this file
if __name__ == "__main__":
    import sys
    # Get the parent directory of the current script (api.py)
    CURR_DIR = os.path.dirname(os.path.abspath(__file__))

    # Add the parent directory to the Python path
    PARENT_DIR = os.path.join(CURR_DIR, "..")  # Go up one level from utils to project folder
    sys.path.append(PARENT_DIR)

from utils.api import API

class Anime:
    @staticmethod
    def get_anime(page=1, page_size=10):
        endpoint = f"/anime"
        querystring = {"page": page, "size": page_size}
        results = API.get(endpoint, params=querystring)
        print (f"\nANIME API Results: {results}")
        return results

if __name__ == "__main__":
    Anime.get_anime()