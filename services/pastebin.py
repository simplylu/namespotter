# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "Pastebin.com is an online platform that allows users to store and share text snippets or code snippets, providing a convenient way to share and collaborate on textual content."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://pastebin.com/u/{username}"
  req: requests.Response = requests.head(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return (req.status_code // 100 == 2, url)
