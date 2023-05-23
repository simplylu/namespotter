# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "Vimeo.com is a video-sharing platform that focuses on high-quality and creative content, providing a space for artists, filmmakers, and professionals to showcase their work and connect with a community of like-minded individuals."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://vimeo.com/{username}"
  req: requests.Response = requests.head(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return (req.status_code // 100 == 2, url)
