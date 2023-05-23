from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "VK.com, also known as VKontakte, is a social networking platform that connects users, primarily from Russia and neighboring countries, enabling them to communicate, share media, join communities, and discover entertainment content."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://vk.com/{username}"
  req: requests.Response = requests.get(url)
  return ("<title>404 Not Found</title>" not in req.text, url)