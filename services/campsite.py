# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "Campsite.bio is an all-in-one link management platform designed for creators, influencers, and businesses, allowing them to create a customizable landing page with multiple links, social media profiles, and promotional content to enhance their online presence and engagement."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://campsite.bio/{username}"
  req: requests.Response = requests.head(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return (req.status_code // 100 == 2, url)
