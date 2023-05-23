from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "Github.com is a widely-used web-based platform that provides hosting for software development projects, allowing developers to collaborate, version control their code, and track issues in a streamlined and accessible manner."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://github.com/{username}/"
  req: requests.Response = requests.get(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return (req.status_code // 100 == 2, url)