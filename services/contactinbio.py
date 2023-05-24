# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "Contactin.bio is a comprehensive contact management platform that allows users to create a customized landing page with multiple contact options, making it easy for others to connect with them through various communication channels."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://{username}.contactin.bio/"
  req: requests.Response = requests.get(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return ("<title>404 - Page not found" not in req.text, url)
