# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "PicsArt.com is a popular creative platform that offers a suite of powerful photo editing tools, artistic filters, and a vibrant community for users to explore, enhance, and share their photos and digital artwork."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://picsart.com/u/{username}"
  req: requests.Response = requests.head(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return (req.status_code // 100 == 2, url)
