from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "Twitch.tv is a popular live streaming platform primarily focused on video game streaming and esports content, but also encompassing a wide range of creative arts and entertainment categories."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://www.twitch.tv/{username}"
  req: requests.Response = requests.get(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return ("player.twitch.tv" in req.text, url)