# from settings import USER_AGENT
from typing import Tuple
import requests

__info__ = "Quora.com is a question-and-answer platform where users can ask questions, share knowledge, and engage in discussions on a wide range of topics, tapping into the collective wisdom and expertise of a diverse community."

def check(username: str) -> Tuple[bool, str]:
  s: requests.Session = requests.session()
  s.headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"
  s.headers["Accept-Encoding"] = "gzip, deflate, br"
  s.headers["Accept-Language"] = "en-US,en;q=0.5"
  s.headers["Alt-Used"] = "www.quora.com"
  s.headers["Host"] = "www.quora.com"
  s.headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0"
  s.get("https://www.quora.com", allow_redirects=False)

  url: str = f"https://www.quora.com/profile/{username}"
  req: requests.Response = s.get(url, allow_redirects=False)
  return (req.status_code // 100 == 2 and username in req.text, url)
