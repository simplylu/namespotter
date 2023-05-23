# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "Bandcamp.com is a music-focused platform that empowers independent artists to showcase, sell, and distribute their music directly to fans, fostering a supportive and direct connection between musicians and their audience."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://bandcamp.com/{username}"
  req: requests.Response = requests.head(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return (req.status_code // 100 == 2, url)
