# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "Letterboxd.com is a film-focused social networking platform that allows users to discover, rate, and review movies, create personalized film diaries, and engage in discussions with a passionate community of cinephiles."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://letterboxd.com/{username}/"
  req: requests.Response = requests.head(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return (req.status_code // 100 == 2, url)
