# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "PayPal.me is a personalized payment link service provided by PayPal, allowing users to easily request and receive money from others by sharing a unique link associated with their PayPal account."

def check(username: str) -> Tuple[bool, str]:
  url: str = f"https://www.paypal.com/paypalme/{username}"
  req: requests.Response = requests.get(url, headers={
    "User-Agent": "curl/8.0.1"
  })
  return (f'<meta property="og:url" content="https://www.paypal.com/paypalme/{username}'.lower() in req.text.lower(), url)
