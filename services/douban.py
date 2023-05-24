# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "Douban.com is a Chinese social networking platform that combines elements of film, book, and music reviews, fostering discussions and recommendations among users based on their shared interests."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://www.douban.com/people/{username}/"
  req: requests.Response = requests.head(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return (req.status_code // 100 == 2, url)
