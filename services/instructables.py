# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "Instructables.com is a platform that allows users to discover, create, and share step-by-step DIY projects and tutorials across a wide range of topics, promoting creativity and knowledge-sharing in a vibrant community."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://www.instructables.com/member/{username}/"
  req: requests.Response = requests.head(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return (req.status_code // 100 == 2, url)
