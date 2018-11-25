# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 19:43:39 2018

@author: divyakamat
"""


import requests

response = requests.get("http://www.aayisrecipes.com/munchies-dabbe-khaan/spicy-shankarpalkharatheek-shankarpal/")

print(response.status_code)

print(response.content)