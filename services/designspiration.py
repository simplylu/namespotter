# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "Designspiration.com is a visual inspiration platform that curates a wide range of design-related content, including images, projects, and ideas, serving as a valuable resource for designers seeking creative inspiration."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://www.designspiration.com/{username}/"
  req: requests.Response = requests.head(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return (req.status_code // 100 == 2, url)
