# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "Gumroad.com is an e-commerce platform that empowers creators and small businesses to sell digital products, subscriptions, and physical goods directly to their audience with ease."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://{username}.gumroad.com/"
  req: requests.Response = requests.head(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return (req.status_code // 100 == 2, url)
