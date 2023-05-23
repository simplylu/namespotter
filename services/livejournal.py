# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "LiveJournal.com is a long-standing blogging platform that combines social networking features, allowing users to publish personal journal entries, connect with friends, and participate in communities, fostering online expression and interaction."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://{username}.livejournal.com"
  req: requests.Response = requests.head(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return (req.status_code // 100 == 2, url)
