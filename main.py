import random
import os 
import math
import datetime
import sys

from my_module import hello

print(hello("Bob"))


import requests

response = requests.get("https://api.github.com")
print(response.status_code)