from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "Twitter.com is a social media platform known for its concise and real-time messaging format, where users can share and discover information, engage in conversations, and follow updates from individuals, organizations, and media outlets."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://twitter.com/{username}"
  req: requests.Response = requests.get(url, headers={
    "User-Agent": USER_AGENT
  })
  return ("player.twitch.tv" in req.text, url)