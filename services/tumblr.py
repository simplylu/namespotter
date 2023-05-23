# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "Tumblr.com is a microblogging and social media platform where users can create and share multimedia posts, follow other blogs, and engage in a community that spans a diverse range of interests and creative expression."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://www.tumblr.com/{username}"
  req: requests.Response = requests.head(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return (req.status_code // 100 == 2, url)
