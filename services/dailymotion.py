# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "Dailymotion.com is a video-sharing platform that offers a diverse range of user-generated and professional content, allowing users to discover, watch, and share videos across various topics and genres."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://www.dailymotion.com/{username}"
  req: requests.Response = requests.head(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return (req.status_code // 100 == 2, url)
