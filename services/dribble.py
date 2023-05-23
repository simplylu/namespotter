# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "Dribbble.com is an online community and platform for designers, providing a space to showcase their creative work, gain inspiration, and connect with other design professionals and potential clients."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://dribbble.com/{username}/about"
  req: requests.Response = requests.head(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return (req.status_code // 100 == 2, url)
