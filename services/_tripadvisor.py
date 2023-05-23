from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "TripAdvisor.com is a widely-used travel platform that provides user-generated reviews, recommendations, and booking options for accommodations, restaurants, and attractions worldwide, helping travelers make informed decisions and plan their trips."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://www.tripadvisor.com/Profile/{username}"
  req: requests.Response = requests.head(url, headers={
    "User-Agent": USER_AGENT
  }, allow_redirects=True)
  return (req.status_code // 100 < 4, url)
