from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "Behance.net is a leading online platform for creative professionals, where artists, designers, and creators can showcase their portfolios, gain exposure, and connect with potential clients and collaborators."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://www.behance.net/{username}/"
  req: requests.Response = requests.head(url, headers={
    "User-Agent": USER_AGENT
  })
  return (req.status_code // 100 == 2, url)