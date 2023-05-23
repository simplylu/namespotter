# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "Flickr.com is a popular photo-sharing platform that enables users to upload, organize, and share their images with others, while also providing a vibrant community for photography enthusiasts to discover and engage with diverse visual content."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://www.flickr.com/people/{username}"
  req: requests.Response = requests.head(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return (req.status_code // 100 == 2, url)
