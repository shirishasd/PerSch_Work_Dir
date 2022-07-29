import requests
import pprint
import json
api_endpoint = "https://cat-fact.herokuapp.com/facts"
response = requests.get(
    api_endpoint
)
pages_response=json.loads(response.text)
pprint.pp(pages_response)
for idx, item in enumerate(response.json()):
    print(idx,item)
    print(f"{idx}. {item['status']}")
    print(f"{idx+1}. {item['status']['verified']},{item['status']['sentCount']}")