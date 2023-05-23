# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "Spotify.com is a leading music streaming platform that offers a vast library of songs, podcasts, and audio content, allowing users to discover, stream, and create personalized playlists tailored to their musical preferences."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://open.spotify.com/user/{username}"
  req: requests.Response = requests.head(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return (req.status_code // 100 == 2, url)
