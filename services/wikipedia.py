from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "Wikipedia.org is a vast collaborative online encyclopedia that provides free, reliable, and crowdsourced information on an extensive range of subjects."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://de.wikipedia.org/wiki/Benutzer:{username}"
  req: requests.Response = requests.get(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return (req.status_code // 100 == 2, url)