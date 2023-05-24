# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "Substack.com is a newsletter platform that empowers writers and journalists to publish and monetize their content directly, fostering a direct connection with their audience and providing a subscription-based model for readers."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://substack.com/@{username}"
  req: requests.Response = requests.head(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return (req.status_code // 100 == 2, url)
