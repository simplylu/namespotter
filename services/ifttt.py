from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "IFTTT.com is an automation platform that enables users to create connections between different apps and devices, allowing them to automate tasks and workflows based on triggers and actions, simplifying digital interactions."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://ifttt.com/p/{username}"
  req: requests.Response = requests.head(url, headers={
    "User-Agent": USER_AGENT
  })
  return (req.status_code // 100 == 2, url)
