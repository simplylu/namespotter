# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "Rumble.com is a video-sharing platform that emphasizes user-generated content, allowing creators to upload, share, and monetize their videos while offering a diverse range of content for viewers to explore."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://rumble.com/user/{username}"
  req: requests.Response = requests.head(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return (req.status_code // 100 == 2, url)
