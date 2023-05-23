# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "Reddit.com is a sprawling online community and discussion platform where users can share, discuss, and vote on a wide variety of content spanning numerous topics, interests, and communities."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://www.reddit.com/user/{username}/"
  req: requests.Response = requests.get(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return ('<meta name="robots" content="noindex,nofollow"/>' not in req.text, url)

check("rezolkasdlkasd")