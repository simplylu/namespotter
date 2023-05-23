from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "About.me is a personal branding platform that allows individuals to create a centralized online profile, showcasing their professional background, interests, and social media presence."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://about.me/{username}"
  req: requests.Response = requests.get(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return (req.status_code // 100 == 2, url)