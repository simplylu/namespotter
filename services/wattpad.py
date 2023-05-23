# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "Wattpad.com is an online storytelling community where users can read, write, and share a wide range of original stories, allowing aspiring writers to showcase their work and engage with a global audience."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://www.wattpad.com/user/{username}"
  req: requests.Response = requests.head(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return (req.status_code // 100 == 2, url)
