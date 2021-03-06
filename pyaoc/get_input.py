#! /usr/bin/env python
import os
import appdirs
import requests
from pathlib import Path

def get_input(year: int, day: int, session: object) -> (str, str):
  """Return cache file input data from cache folder for certain problem"""
  cache_file = Path(os.path.join(appdirs.user_cache_dir(appname="AdventOfCode"), session.get('name'), str(year), str(day), 'input'))
  input_data = None
  if not cache_file.exists():
    input_data = requests.get(f'https://adventofcode.com/{year}/day/{day}/input', cookies={'session': session.get('value')}).text
    if "before it unlocks!" in input_data:
      return None, "Please don't repeatedly request this endpoint before it unlocks! The calendar countdown is synchronized with the server time; the link will be enabled on the calendar the instant this puzzle becomes available."
    Path(os.path.dirname(cache_file)).mkdir(parents=True, exist_ok=True)
    with open(cache_file, "w+") as opened_file:
      opened_file.write(input_data)
  else:
    with open(cache_file) as opened_file:
      input_data = opened_file.read()
  return input_data, ''