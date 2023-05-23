from importlib import import_module
from types import ModuleType
from typing import Dict, Tuple
from colorama import Fore

GREEN: str = Fore.GREEN
RED: str = Fore.RED
RESET: str = Fore.RESET

tests: Dict[str, Dict[str, str]] = {
  "twitch": {
    "existing_user": "rezo",
    "nonexisting_user": "rezolkasdlkasd"
  },
  "youtube": {
    "existing_user": "renzo69",
    "nonexisting_user": "renzo69lkasdlkasd"
  },
  "instagram": {
    "existing_user": "rezo",
    "nonexisting_user": "rezolkasdlkasd"
  },
  "tiktok": {
    "existing_user": "rezo",
    "nonexisting_user": "rezolkasdlkasd"
  },
  "wordpress": {
    "existing_user": "rezo",
    "nonexisting_user": "rezolkasdlkasd"
  },
  "blogger": {
    "existing_user": "rezo",
    "nonexisting_user": "rezolkasdlkasd"
  },
  "pinterest": {
    "existing_user": "rezo",
    "nonexisting_user": "rezolkasdlkasd"
  },
  "wikipedia": {
    "existing_user": "Gardini",
    "nonexisting_user": "Gardinilkasdlkasd"
  },
  "aboutme": {
    "existing_user": "rezo",
    "nonexisting_user": "rezolkasdlkasd"
  },
  "github": {
    "existing_user": "rezo",
    "nonexisting_user": "rezolkasdlkasd"
  },
  "linktree": {
    "existing_user": "rezo",
    "nonexisting_user": "rezolkasdlkasd"
  },
  "vk": {
    "existing_user": "hannes",
    "nonexisting_user": "hanneslkasdlkasd"
  },
  "vimeo": {
    "existing_user": "hans",
    "nonexisting_user": "hanslkasdlkasd"
  },
  "wattpad": {
    "existing_user": "hannah",
    "nonexisting_user": "hannahlkasdlkasd"
  },
  "spotify": {
    "existing_user": "rezo",
    "nonexisting_user": "rezolkasdlkasd"
  },
  "steamcommunity": {
    "existing_user": "rezo",
    "nonexisting_user": "rezolkasdlkasd"
  },
  "pastebin": {
    "existing_user": "rezo",
    "nonexisting_user": "rezolkasdlkasd"
  },
  "bandcamp": {
    "existing_user": "rezo",
    "nonexisting_user": "rezolkasdlkasd"
  },
  "behance": {
    "existing_user": "hannes",
    "nonexisting_user": "hanneslkasdlkasd"
  },
  "buzzfeed": {
    "existing_user": "hannes",
    "nonexisting_user": "hanneslkasdlkasd"
  },
  "blipfm": {
    "existing_user": "rezo",
    "nonexisting_user": "rezolkasdlkasd"
  },
  "cashapp": {
    "existing_user": "rezo",
    "nonexisting_user": "rezolkasdlkasd"
  },
  "paypal": {
    "existing_user": "rezo",
    "nonexisting_user": "rezolkasdlkasd"
  },
  "tumblr": {
    "existing_user": "hannes",
    "nonexisting_user": "hanneslkasdlkasd"
  },
  "trakttv": {
    "existing_user": "hannes",
    "nonexisting_user": "hanneslkasdlkasd"
  },
  "soundcloud": {
    "existing_user": "rezo",
    "nonexisting_user": "rezolkasdlkasd"
  },
  "slideshare": {
    "existing_user": "rezo",
    "nonexisting_user": "rezolkasdlkasd"
  },
  "slack": {
    "existing_user": "rezo",
    "nonexisting_user": "rezolkasdlkasd"
  },
  "scribd": {
    "existing_user": "rezo",
    "nonexisting_user": "rezolkasdlkasd"
  },
  "roblox": {
    "existing_user": "hannes",
    "nonexisting_user": "hanneslkasdlkasd"
  },
  "reverbnation": {
    "existing_user": "rezo",
    "nonexisting_user": "rezolkasdlkasd"
  },
  "patreon": {
    "existing_user": "rezo",
    "nonexisting_user": "rezolkasdlkasd"
  },
  "newgrounds": {
    "existing_user": "rezo",
    "nonexisting_user": "rezolkasdlkasd"
  },
  "medium": {
    "existing_user": "rezo",
    "nonexisting_user": "rezolkasdlkasd"
  },
  "livejournal": {
    "existing_user": "rezo",
    "nonexisting_user": "rezolkasdlkasd"
  },
  "lastfm": {
    "existing_user": "rezo",
    "nonexisting_user": "rezolkasdlkasd"
  },
  "kongregate": {
    "existing_user": "rezo",
    "nonexisting_user": "rezolkasdlkasd"
  },
  "keybase": {
    "existing_user": "rezo",
    "nonexisting_user": "rezolkasdlkasd"
  },
  "instructables": {
    "existing_user": "hannes",
    "nonexisting_user": "hanneslkasdlkasd"
  },
  "ifttt": {
    "existing_user": "rezo",
    "nonexisting_user": "rezolkasdlkasd"
  },
  "hubpages": {
    "existing_user": "hannes",
    "nonexisting_user": "hanneslkasdlkasd"
  },
  "houzz": {
    "existing_user": "rezo",
    "nonexisting_user": "rezolkasdlkasd"
  },
  "ycombinator": {
    "existing_user": "rezo",
    "nonexisting_user": "rezolkasdlkasd"
  },
  "gumroad": {
    "existing_user": "rezo",
    "nonexisting_user": "rezolkasdlkasd"
  },
  "gravatar": {
    "existing_user": "hannes",
    "nonexisting_user": "hanneslkasdlkasd"
  },
  "goodreads": {
    "existing_user": "rezo",
    "nonexisting_user": "rezolkasdlkasd"
  },
  "flipboard": {
    "existing_user": "rezo",
    "nonexisting_user": "rezolkasdlkasd"
  },
  "flickr": {
    "existing_user": "rezo",
    "nonexisting_user": "rezolkasdlkasd"
  },
  "etsy": {
    "existing_user": "rezo",
    "nonexisting_user": "rezolkasdlkasd"
  },
  "ello": {
    "existing_user": "hannes",
    "nonexisting_user": "hanneslkasdlkasd"
  },
  "dribble": {
    "existing_user": "rezo",
    "nonexisting_user": "rezolkasdlkasd"
  },
  "disqus": {
    "existing_user": "rezo",
    "nonexisting_user": "rezolkasdlkasd"
  },
  "deviantart": {
    "existing_user": "rezo",
    "nonexisting_user": "rezolkasdlkasd"
  },
  "designspiration": {
    "existing_user": "rezo",
    "nonexisting_user": "rezolkasdlkasd"
  },
  "dailymotion": {
    "existing_user": "rezo",
    "nonexisting_user": "rezolkasdlkasd"
  },
  "creativemarket": {
    "existing_user": "rezo",
    "nonexisting_user": "rezolkasdlkasd"
  },
  "colourlovers": {
    "existing_user": "Trixxie",
    "nonexisting_user": "Trixxielkasdlkasd"
  },
  "quora": {
    "existing_user": "Hannes",
    "nonexisting_user": "Hanneslkasdlkasd"
  },
  "picsart": {
    "existing_user": "oriartbr",
    "nonexisting_user": "oriartbrlkasdlkasd"
  },
  "likee": {
    "existing_user": "rezo",
    "nonexisting_user": "rezolkasdlkasd"
  },
  "untappd": {
    "existing_user": "shanecmiller",
    "nonexisting_user": "shanecmillerlkasdlkasd"
  },
  "elpha": {
    "existing_user": "sophiavaldez",
    "nonexisting_user": "sophiavaldezlkasdlkasd"
  },
  "steemit": {
    "existing_user": "rezo",
    "nonexisting_user": "rezolkasdlkasd"
  },
  "bebee": {
    "existing_user": "ana-filgueira",
    "nonexisting_user": "ana-filgueiralkasdlkasd"
  },
  "fark": {
    "existing_user": "Sliding Carp",
    "nonexisting_user": "Sliding Carplkasdlkasd"
  },
  "mix": {
    "existing_user": "rezo",
    "nonexisting_user": "rezolkasdlkasd"
  },
  "skyrock": {
    "existing_user": "katchann",
    "nonexisting_user": "katchannlkasdlkasd"
  },
  "influenster": {
    "existing_user": "summah",
    "nonexisting_user": "summahlkasdlkasd"
  },
}


import sys
if len(sys.argv) != 1:
  check_only = sys.argv[1]
  skip = True
else:
  skip = False
  check_only = ""

for idx, (name, conditions) in enumerate(tests.items()):
  if skip and name != check_only:
    continue
  service: ModuleType = import_module(f".{name}", "services")
  print(f"[ ] Checking {idx}/{len(tests)} {name}", end='\r')
  res1: Tuple[bool, str] = service.check(conditions["existing_user"])
  res2: Tuple[bool, str] = service.check(conditions["nonexisting_user"])
  if not res1[0] or res2[0]:
    print(f"[{RED}E{RESET}] Error validating {name}; please check manually for existing user {conditions['existing_user']} and non existing user {conditions['nonexisting_user']} to repair the check logic")
  else:
    print(f"[{GREEN}*{RESET}] Checking {idx+1}/{len(tests)} {name}")