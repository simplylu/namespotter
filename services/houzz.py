# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "Houzz.com is a comprehensive home improvement and design platform that offers inspiration, product recommendations, and professional services to homeowners, serving as a hub for all things related to home remodeling and decoration."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://www.houzz.com/user/{username}"
  req: requests.Response = requests.head(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return (req.status_code // 100 == 2, url)
