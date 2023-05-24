# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "Lnk.bio is a link management platform that allows users to create a customized landing page with multiple links, making it easier to share and navigate various online profiles and content in one central location."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://lnk.bio/{username}"
  req: requests.Response = requests.head(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return (req.status_code // 100 == 2, url)
