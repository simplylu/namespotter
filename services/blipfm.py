# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "Blip.fm was a social music streaming platform that allowed users to discover, share, and listen to music in a personalized radio-style format, but it is no longer in active operation as of 2021."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://blip.fm/{username}"
  req: requests.Response = requests.head(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return (req.status_code // 100 == 2, url)
