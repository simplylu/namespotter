# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "Scribd.com is a digital library and document sharing platform offering a vast collection of books, audiobooks, magazines, and documents, accessible through a subscription model, providing a comprehensive resource for reading and research."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://www.scribd.com/{username}"
  req: requests.Response = requests.head(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return (req.status_code // 100 < 4, url)
