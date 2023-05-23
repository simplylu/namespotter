# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "Ello.co is a social networking platform that emphasizes ad-free, creative expression and community engagement, providing a space for artists, designers, and enthusiasts to share their work and connect with like-minded individuals."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://ello.co/{username}"
  req: requests.Response = requests.get(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return ("<title>Ello | Be inspired. | [404] Not Found</title>".lower() not in req.text.lower(), url)
