#
# Created on Tue May 23 2023
#
# Copyright (c) 2023 simplylu
#
# Imports
from importlib import import_module
from threading import Thread
from time import time
import sys
import os

# Type Annotations
from typing import List, Tuple
from types import ModuleType


# Constants / Globals
SERVICE_DIR: str = os.path.join(os.getcwd(), "services")
SERVICES: List[str] = [path.split(".")[0] for path in os.listdir(SERVICE_DIR) if not path.startswith("_")]
SERVICE_COUNT: int = len(SERVICES)
THREADS: int = 8
FINDINGS: List[Tuple[str, str]] = []
HEADER: str = """     _   __                    _____             __  __           
    / | / /___ _____ ___  ___ / ___/____  ____  / /_/ /____  _____
   /  |/ / __ `/ __ `__ \/ _ \\__ \/ __ \/ __ \/ __/ __/ _ \/ ___/
  / /|  / /_/ / / / / / /  __/__/ / /_/ / /_/ / /_/ /_/  __/ /    
 /_/ |_/\__,_/_/ /_/ /_/\___/____/ .___/\____/\__/\__/\___/_/     
(c) 2023 by simplylu (@s1mplylu)/_/ """

# Methods
def load_service(name: str) -> ModuleType:
  return import_module(f".{name}", "services")

def progress(count: int, name: str) -> None:
  print(f"Progress: {str(-count+SERVICE_COUNT).rjust(len(str(SERVICE_COUNT)), ' ')}/{SERVICE_COUNT} - {name.ljust(20, ' ')}", end='\r')

def threaded_function(username: str) -> None:
  global SERVICES, FINDINGS
  while SERVICES:
    name: str = SERVICES.pop(0)
    progress(len(SERVICES), name)
    service: ModuleType = load_service(name)
    res: Tuple[str, str] = service.check(username)
    if res[0]:
      FINDINGS.append((name, res[1]))


# Main
def main() -> None:
  print(HEADER)
  global FINDINGS
  if len(sys.argv) == 1:
    print(f"Usage: {sys.argv[0]} <username>")
    exit(1)

  username = sys.argv[1]
  procs: List[Thread] = [
      Thread(target=threaded_function, args=(username, )) for _ in range(THREADS)
  ]
  time_start = time()
  for proc in procs:
    proc.start()
  for proc in procs:
    proc.join()
  
  time_end = time()
  
  print()
  for finding in FINDINGS:
    print(f"Found on {finding[0]} :: {finding[1]}")
    # Do it later via logging
  
  print(f"\nFound {len(FINDINGS)} services for username {username}")
  print(f"Took {round(time_end-time_start, 2)}s to run")
  print("Ch33rs, Lu <3")


# Driver
if __name__ == "__main__":
  main()
  exit(0)
else:
  print("Cannot be imported as a module!")
