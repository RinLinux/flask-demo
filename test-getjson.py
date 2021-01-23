# encoding: utf-8

"""
date: 2021/01/22/22/39

"""

import requests
import json

url = 'http://127.0.0.1:5000/getjson'

r = requests.get(url)

for item in json.loads(r.text):
    print(item)