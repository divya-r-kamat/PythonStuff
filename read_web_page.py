# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 19:43:39 2018

@author: divyakamat
"""


import requests

response = requests.get("https://en.wikipedia.org/wiki/main_page")

print(response.status_code)

print(response.content.decode("utf-8").find("Did you know"))