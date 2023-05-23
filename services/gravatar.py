# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "Gravatar.com is a globally recognized avatar service that allows users to associate a unique profile picture with their email address, which is automatically displayed on various websites and platforms that support Gravatar integration."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://en.gravatar.com/{username}"
  req: requests.Response = requests.head(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return (req.status_code // 100 == 2, url)
