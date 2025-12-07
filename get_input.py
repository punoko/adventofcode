import argparse
import datetime
import os
import sys

import requests

DECEMBER = 12
tz = datetime.timezone(offset=datetime.timedelta(hours=-5))  # UTC-5
today = datetime.datetime.now(tz=tz).date()
year = today.year if today.month == DECEMBER else today.year - 1
day = today.day if today.month == DECEMBER else None

parser = argparse.ArgumentParser(description="Get AoC input")
parser.add_argument("-y", "--year", type=int, default=year, help="default: %(default)s")
parser.add_argument("-d", "--day", type=int, default=day, help="default: %(default)s")
args = parser.parse_args()

url = f"https://adventofcode.com/{args.year}/day/{args.day}/input"
try:
    cookies = {"session": os.environ["SESSION"]}
except KeyError:
    sys.exit("SESSION environment variable containing session cookie required")

response = requests.get(url=url, cookies=cookies, timeout=3)
print(args.year, "day", args.day, file=sys.stderr)
print(response.text.strip())
response.raise_for_status()
