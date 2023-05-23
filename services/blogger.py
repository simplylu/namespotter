from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "Blogspot.com, also known as Blogger, is a popular blogging platform that enables users to create and publish their own blogs with ease, offering various customization options and integration with Google services."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"http://{username}.blogspot.com/"
  req: requests.Response = requests.head(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return (req.status_code // 100 == 2, url)