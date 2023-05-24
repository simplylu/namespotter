# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "italki.com is an online language learning platform that connects language learners with qualified tutors for personalized language lessons through video chat, helping users improve their language skills from the comfort of their own homes."

def check(username: str) -> Tuple[bool, str]:
  url: str = "https://api.italki.com/api/v2/teachers"
  data: dict = {"keyword":username,"page_size":20,"user_timezone":"Europe/Berlin","page":1}
  req: requests.Response = requests.post(url, data=data)
  return (req.json()["paging"]["total"] == 1, url)
