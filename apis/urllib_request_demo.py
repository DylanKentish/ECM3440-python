# urllib_request_demo.py

# See https://data.police.uk/docs/ for details of available API calls 
api_url:str = "http://data.police.uk/api/devon-and-cornwall/DEV.4055/people"

import urllib.request
import json

data:list = []

with urllib.request.urlopen(api_url) as f:
    data_text:str = f.read().decode('utf-8')
    data = json.loads(data_text)

for record in data:
    print(record["name"], record["rank"])
