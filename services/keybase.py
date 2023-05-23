# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "Keybase.io is a platform that combines encrypted messaging, file sharing, and identity verification, providing a secure and user-friendly environment for communication and collaboration."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://keybase.io/{username}"
  req: requests.Response = requests.head(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return (req.status_code // 100 == 2, url)
