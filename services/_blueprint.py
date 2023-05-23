import requests

__info__ = "Twitch.tv is a popular live streaming platform primarily focused on video game streaming and esports content, but also encompassing a wide range of creative arts and entertainment categories."

def check(username: str) -> bool:
  url: str = f"https://www.twitch.tv/{username}"
  req: requests.Response = requests.get(url)
  return ("<meta property='twitter:site' content='@twitch'>" in req.text, url)