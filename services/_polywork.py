# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "Polywork.com is a professional networking platform that showcases users' diverse skills, projects, and experiences, providing a comprehensive view of their multifaceted professional identities."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://www.polywork.com/{username}"
  req: requests.Response = requests.get(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return (req.status_code // 100 == 2, url)
