# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "GaiaOnline.com is an online community and virtual world where users can create avatars, engage in role-playing, and interact with other members through forums, games, and various social activities."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://www.gaiaonline.com/profiles/{username}/"
  req: requests.Response = requests.get(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return ("<title>General Error | Gaia Online</title>" not in req.text, url)
