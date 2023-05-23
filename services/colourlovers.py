from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "Colourlovers.com is a vibrant online community and resource for color inspiration, providing a platform for users to explore, create, and share color palettes, patterns, and designs."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://www.colourlovers.com/lover/{username}"
  req: requests.Response = requests.head(url, headers={
    "User-Agent": USER_AGENT
  })
  return (req.status_code // 100 == 2, url)
