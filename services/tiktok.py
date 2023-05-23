from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "TikTok.com is a highly engaging video-sharing platform known for its short-form and creative content, where users can create, discover, and share entertaining videos across a wide range of topics and trends."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://www.tiktok.com/@{username}?lang=en"
  req: requests.Response = requests.get(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return ('<title data-rh="true"> | TikTok</title>' not in req.text, url)