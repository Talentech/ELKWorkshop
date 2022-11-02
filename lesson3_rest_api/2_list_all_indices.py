from textwrap import indent
import requests
from pprint import pprint

url = 'http://localhost:9200/_cat/indices?v'
response = requests.get(url)

pprint(response.text)
