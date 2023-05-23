# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "Mix.com is a content discovery platform that personalizes and recommends articles, videos, and other web content based on users' interests, providing a convenient way to explore and save interesting content from across the web."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://mix.com/{username}"
  req: requests.Response = requests.head(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return (req.status_code // 100 == 2, url)
