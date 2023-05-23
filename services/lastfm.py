# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "Last.fm is a music streaming and recommendation platform that tracks users' listening habits, provides personalized music recommendations, and connects music enthusiasts with similar tastes in an engaging online community."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://www.last.fm/user/{username}"
  req: requests.Response = requests.head(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return (req.status_code // 100 == 2, url)
