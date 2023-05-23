# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "OnlyFans.com is a subscription-based platform that allows creators to share exclusive content with their subscribers, primarily known for its adult content, but also used by artists, influencers, and other content creators."

def check(username: str) -> Tuple[bool, str]:
  s: requests.Session = requests.session()
  # Getting first CSRF Token
  req: requests.Response = s.get("https://static.onlyfans.com/theme/onlyfans/spa/app.js?rev=202305231059-a7f490cb74")
  csrf_token = req.text.split(",k=\"")[1].split("\"")[0]
  print(csrf_token)
  # url: str = f"https://www.youtube.com/{username}"
  # req: requests.Response = requests.head(url, headers={
  #   "User-Agent": "curl/8.0.1"
  # })
  # return (req.status_code // 100 == 2, url)

check("hannahh")