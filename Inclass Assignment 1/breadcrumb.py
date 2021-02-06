import json
import urllib.request
import os
import pandas as pd

with urllib.request.urlopen('http://rbi.ddns.net/getBreadCrumbData')as response:
    breadcrumb = response.read()

data = json.loads(breadcrumb)
#print(data[0:1000])
#data = json.loads(json_string
#for k in range(1, 1000):
    #print(data[k])

with open('bread_crumb_data.json', 'w') as file:
    json.dump(data[:1000], file)
