# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "Likee.video is a dynamic short video platform that allows users to create and share creative videos, discover trending content, and engage with a global community through innovative video editing features and interactive challenges."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://likee.video/@{username}"
  req: requests.Response = requests.head(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return (req.status_code // 100 == 2, url)
