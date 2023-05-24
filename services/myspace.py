# from settings import USER_AGENT
from typing import Tuple
import requests
import urllib3

urllib3.disable_warnings()

__info__ = "Myspace.com is a former social networking platform that gained popularity in the early 2000s, allowing users to create personal profiles, connect with friends, and discover music and entertainment content."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://myspace.com/{username}"
  req: requests.Response = requests.head(url, verify=False, headers={
    "User-Agent": "curl/8.0.1"
  })
  return (req.status_code // 100 == 2, url)
