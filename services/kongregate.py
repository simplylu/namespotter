# from settings import USER_AGENT
from typing import Tuple
import urllib3
urllib3.disable_warnings()
import requests

__info__ = "Kongregate.com is an online gaming platform that offers a vast collection of free-to-play games, ranging from casual to more complex genres, providing an entertaining and community-driven gaming experience."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"http://www.kongregate.com/accounts/{username}"
  req: requests.Response = requests.head(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return (req.status_code // 100 == 2, url)
