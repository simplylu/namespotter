# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "Trakt.tv is a platform dedicated to tracking and organizing users' TV shows and movies, offering features such as personalized recommendations, watchlist management, and social interactions with other entertainment enthusiasts."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://trakt.tv/users/{username}"
  req: requests.Response = requests.head(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return (req.status_code // 100 == 2, url)
