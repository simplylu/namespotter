# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "ReverbNation.com is a music-focused platform that provides tools for artists to promote their music, connect with fans, book gigs, and access industry opportunities, supporting independent musicians in their career development."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://www.reverbnation.com/{username}/"
  try:
      req: requests.Response = requests.head(url, headers={
      "User-Agent": "curl/8.0.1"
    }, timeout=5)
  except Exception:
    return (False, "")
  return (req.status_code // 100 == 2, url)
