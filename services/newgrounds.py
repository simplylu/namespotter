# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "Newgrounds.com is an online entertainment platform that hosts user-generated content such as animations, games, and artwork, providing a space for creativity and community interaction within the digital arts."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://{username}.newgrounds.com/"
  req: requests.Response = requests.head(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return (req.status_code // 100 == 2, url)
