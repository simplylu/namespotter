# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "Untappd.com is a social networking platform for beer enthusiasts, allowing users to discover, rate, and share their favorite beers, explore new breweries, and connect with fellow beer lovers."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://untappd.com/user/{username}"
  req: requests.Response = requests.head(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return (req.status_code // 100 == 2, url)
