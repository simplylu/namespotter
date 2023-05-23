# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "Slideshare.net is a platform for sharing and discovering professional presentations, documents, and infographics, providing a valuable resource for knowledge sharing and learning across various industries and topics."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://www.slideshare.net/{username}"
  req: requests.Response = requests.head(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return (req.status_code // 100 == 2, url)
