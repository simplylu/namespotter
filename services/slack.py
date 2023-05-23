# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "Slack.com is a widely-used collaboration platform that facilitates team communication, file sharing, and project management, enhancing productivity and streamlining workflows for organizations of all sizes."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://{username}.slack.com/"
  req: requests.Response = requests.head(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return (req.status_code // 100 != 4, url)
