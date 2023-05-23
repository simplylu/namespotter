from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "CreativeMarket.com is an online marketplace that provides a platform for independent creators to sell and purchase design assets, including graphics, templates, fonts, and more, supporting the creative community with a wide range of digital resources."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://creativemarket.com/users/{username}"
  req: requests.Response = requests.head(url, headers={
    "User-Agent": USER_AGENT
  })
  return (req.status_code // 100 == 2, url)
