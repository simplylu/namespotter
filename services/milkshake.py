# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "Milkshake.app is a user-friendly mobile website builder that enables users to create stylish and personalized single-page websites directly from their smartphones, perfect for showcasing portfolios, businesses, and personal brands."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://msha.ke/{username}"
  req: requests.Response = requests.head(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return (req.status_code // 100 == 2, url)
