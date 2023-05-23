# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "Medium.com is a popular online publishing platform where writers, journalists, and experts can share their articles and stories with a wide audience, while fostering a community of readers and facilitating thoughtful discussions."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://www.youtube.com/{username}"
  req: requests.Response = requests.get(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return ("<title>404 Not Found</title>" not in req.text, url)
