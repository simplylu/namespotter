# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "Flipboard.com is a personalized news aggregation platform that curates and delivers articles, stories, and multimedia content based on users' interests, allowing for a tailored and immersive reading experience."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://flipboard.com/@{username}"
  req: requests.Response = requests.head(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  open("yes.html", "w").write(req.text)
  return (req.status_code // 100 < 4, url)
