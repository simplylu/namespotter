# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "MyAnimeList.com is a popular online platform for anime and manga enthusiasts, offering a comprehensive database, user reviews, and community features to discover, track, and discuss their favorite anime and manga titles."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://myanimelist.net/profile/{username}"
  req: requests.Response = requests.head(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return (req.status_code // 100 == 2, url)
