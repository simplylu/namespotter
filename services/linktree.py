# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "Linktr.ee is a popular link management tool that allows users, particularly content creators and businesses, to create a customizable landing page containing multiple links to various online platforms and resources."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://linktr.ee/{username}"
  req: requests.Response = requests.head(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return (req.status_code // 100 == 2, url)
