## Lesson 3 - Using ElasticSearch REST API

### 1. ElasticSearch healthcheck

DevTools:
```
GET /
```

Python:
```
from textwrap import indent
import requests
from pprint import pprint

url = 'http://localhost:9200'

response = requests.get(url)

pprint(response.json())

```

### 2. List all elasticsearch indices

DevTools:
```
GET /_cat/indices?v
```

Python:
```
from textwrap import indent
import requests
from pprint import pprint

url = 'http://localhost:9200/_cat/indices?v'
response = requests.get(url)

pprint(response.text)


```

### 3. Insert simple document

DevTools:
```
POST my-index-000001/_doc
{
    "@timestamp": "2022-11-03T08:14:14.485760",
    "level": "Information",
    "message": "Hello, World from REST API via python!",
    "fields": {
      "Platform": "Talentech",
      "Solution": "Workshop",
      "AppName": "Lesson2",
      "EnvironmentName": "Local"
    }
}
```

Python:
```
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

```

### 4 Query documents

Search for all documents that contain *python* keyword 

DevTools:
```
GET /my-index-000001/_search?q=python
```

Search for first two documents that contain field AppName: Lesson2 and show particular values

DevTools:
```
POST /my-index-000001/_search
{
    "query": {
        "match" : {
            "fields.AppName" : "Lesson2"
        }
    },
    "size": 2,
    "from": 0,
    "_source": [ "message", "fields.Platform", "fields.Solution" ],
    "highlight": {
        "fields" : {
            "fields.AppName" : {}
        }
    }
}

```

You can access _id value that identifies given document and use it to delete some documents:

### 5 Delete document

DevTools:
```
DELETE /my-index-000001/_doc/<_id>
```

Reference: [ElasticSearch API](https://www.elastic.co/guide/en/elasticsearch/reference/7.17/docs.html)

