from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "Influenster.com is an online platform where users can discover and review products, share their opinions, and engage with a community of influencers, providing valuable insights and recommendations for various consumer goods and brands."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://www.influenster.com/profile/{username}"
  req: requests.Response = requests.head(url, headers={
    "User-Agent": USER_AGENT
  })
  return (req.status_code // 100 == 2, url)
