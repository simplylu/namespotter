# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "DeviantArt.com is an online community and art platform that enables artists of various genres to showcase their artwork, connect with fellow creators, and engage in a supportive environment for artistic expression and appreciation."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://www.deviantart.com/{username}"
  req: requests.Response = requests.head(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return (req.status_code // 100 == 2, url)
