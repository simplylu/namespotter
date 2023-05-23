# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "Steemit.com is a blockchain-based social media platform where users can create, curate, and engage with content, earning cryptocurrency rewards for their contributions."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://steemit.com/@{username}"
  req: requests.Response = requests.head(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return (req.status_code // 100 == 2, url)
