# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "Goodreads.com is a social platform for book lovers, offering a vast database of user-generated book reviews, recommendations, and a community-driven space for discussing literature and discovering new reads."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://www.goodreads.com/{username}"
  req: requests.Response = requests.get(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return ("<title>Page not found</title>" not in req.text, url)
