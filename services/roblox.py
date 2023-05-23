# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "Roblox.com is an immersive online platform that allows users to create, play, and share games and virtual experiences, fostering a vibrant community of game developers and players."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://www.roblox.com/users/profile?username={username}"
  req: requests.Response = requests.head(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return (req.headers.get("location") != "https://www.roblox.com/request-error?code=404", url)