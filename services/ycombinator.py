# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "News.ycombinator.com is a community-driven platform that features a curated selection of technology news, articles, and discussions, showcasing the latest developments and insights from the tech industry and beyond."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://news.ycombinator.com/user?id={username}"
  req: requests.Response = requests.get(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return ("No such user." not in req.text, url)
