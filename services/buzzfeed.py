# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "Buzzfeed.com is a digital media platform known for its entertaining and shareable content, offering a mix of news, quizzes, lists, and viral articles that cater to a wide range of interests and pop culture trends."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://www.buzzfeed.com/{username}"
  req: requests.Response = requests.head(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return (req.status_code // 100 == 2, url)
