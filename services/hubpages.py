# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "HubPages.com is an online publishing platform where users can create and share informative articles on various topics, engage with a community of writers, and earn revenue through advertising and affiliate programs."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://hubpages.com/@{username}"
  req: requests.Response = requests.head(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return (req.status_code // 100 == 2, url)
