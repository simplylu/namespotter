# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "Skyrock.com is a social networking platform that allows users to create personalized blogs, share multimedia content, and connect with a community of users with shared interests."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://{username}.skyrock.com/"
  req: requests.Response = requests.head(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return (req.status_code // 100 == 2, url)
