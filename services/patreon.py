# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "Patreon.com is a membership platform that enables creators to receive recurring financial support from their fans and followers, allowing them to monetize their content and engage with a dedicated community."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://www.patreon.com/{username}/creators"
  req: requests.Response = requests.head(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return (req.status_code // 100 < 4, url)
