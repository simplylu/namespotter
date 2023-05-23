from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "Pinterest.com is a visually-focused social media platform where users can discover, save, and share inspiring ideas and images across a wide range of interests and topics."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://www.pinterest.com/{username}/"
  req: requests.Response = requests.get(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return ('<title>User Avatar</title>' not in req.text, url)