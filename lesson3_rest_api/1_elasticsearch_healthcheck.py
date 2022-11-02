from textwrap import indent
import requests
from pprint import pprint

url = 'http://localhost:9200'

response = requests.get(url)

pprint(response.json())
