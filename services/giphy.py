# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "YouTube.com is a widely-used video-sharing platform that allows users to upload, watch, and interact with a vast array of user-generated and professional content spanning various topics and genres."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://giphy.com/{username}"
  req: requests.Response = requests.head(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return (req.status_code // 100 == 2, url)
