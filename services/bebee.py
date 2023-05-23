# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "BeBee.com is a professional networking platform that combines elements of social media and job searching, allowing users to showcase their personal brand, connect with industry professionals, and discover career opportunities in a vibrant community."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://br.bebee.com/bee/{username}"
  req: requests.Response = requests.head(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return (req.status_code // 100 == 2, url)
