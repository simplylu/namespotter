# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "Disqus.com is a widely-used commenting platform that allows website owners to integrate a robust and interactive commenting system into their websites, fostering engagement and discussion among visitors."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://disqus.com/by/{username}/"
  req: requests.Response = requests.head(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return (req.status_code // 100 == 2, url)
