from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "Instagram.com is a popular social media platform that emphasizes visual content, enabling users to share photos and videos, discover creative inspiration, and engage with a global community."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://www.instagram.com/{username}/"
  req: requests.Response = requests.get(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return ("<title>Instagram</title>" not in req.text, url)