# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "Elpha.com is an online community and platform designed for women in tech and entrepreneurship, providing a supportive space for networking, mentorship, and knowledge sharing to empower women in their professional journeys."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://elpha.com/members/{username}"
  req: requests.Response = requests.head(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return (req.status_code // 100 == 2, url)
