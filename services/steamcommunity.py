from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "Steamcommunity.com is a social hub integrated with the Steam gaming platform, enabling gamers to connect, share content, join communities, and engage in discussions related to gaming and game development."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://steamcommunity.com/id/{username}"
  req: requests.Response = requests.get(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return ('<title>Steam Community :: Error</title>' not in req.text, url)