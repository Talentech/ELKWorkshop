import requests
from datetime import datetime
from pprint import pprint

index = 'my-index'

url = 'http://localhost:9200/{}-000001/_doc'.format(index)
data = {
  "@timestamp": datetime.utcnow().isoformat(),
  "level": "Information",
  "message": "Hello, World from REST API via python!",
  "fields": {
    "Platform": "Talentech",
    "Solution": "Workshop",
    "AppName": "Lesson2",
    "EnvironmentName": "Local"
  }
}

response = requests.post(url, json=data, headers={'Content-type': 'application/json'})

pprint(response.json())