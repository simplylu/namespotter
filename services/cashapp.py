# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "Cash.me (now known as Cash App) is a mobile payment platform that enables users to send and receive money, make purchases, and manage their finances through a simple and user-friendly interface."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://cash.app/${username}"
  req: requests.Response = requests.head(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return (req.status_code // 100 < 4, url)
