# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "SoundCloud.com is a popular online audio distribution platform that enables musicians, podcasters, and other audio creators to upload, share, and promote their audio content while connecting with a diverse community of listeners."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://soundcloud.com/{username}"
  req: requests.Response = requests.head(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return (req.status_code // 100 == 2, url)
