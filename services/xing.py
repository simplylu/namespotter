# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "Xing.com is a professional networking platform that facilitates business connections, career development, and industry networking, enabling users to showcase their professional profiles and engage with a global community of professionals."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://www.xing.com/profile/{username}"
  req: requests.Response = requests.head(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return (req.status_code // 100 == 2, url)
