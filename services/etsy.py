# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "Etsy.com is an online marketplace that connects independent sellers and buyers, offering a wide range of unique and handmade products, vintage items, and craft supplies."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://www.etsy.com/de-en/people/{username}"
  req: requests.Response = requests.head(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return (req.status_code // 100 == 2, url)
