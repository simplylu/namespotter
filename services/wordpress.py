from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "WordPress.com is a user-friendly online platform that allows individuals and businesses to create and host websites or blogs without the need for advanced coding knowledge."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://{username}.wordpress.com/"
  req: requests.Response = requests.get(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return ('<title>WordPress.com</title>' not in req.text, url)