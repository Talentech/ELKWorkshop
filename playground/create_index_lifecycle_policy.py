import requests

index = 'my-index'
elasticsearch_url = 'http://localhost:9200/'

def createIndexTemplate():
    print('Creating index pattern...')
    url = '{}_template/{}_template'.format(elasticsearch_url, index)
    data = {
        "index_patterns": ["{}*".format(index)],                 
        "settings": {
            "number_of_shards": 3,
            "number_of_replicas": 1,
            "index.lifecycle.name": "{}-policy".format(index),      
            "index.lifecycle.rollover_alias": index  
        }
    }

    response = requests.put(url, json=data, headers={'Content-type': 'application/json'})
    print("done." if response.ok else "FAILED")

def createIndex():
    print('Creating index...')
    url = '{}{}-000001'.format(elasticsearch_url, index)
    data = {
        "settings": {
            "index": {
            "number_of_shards": 3,  
            "number_of_replicas": 2 
            }
        }
    }

    response = requests.put(url, json=data, headers={'Content-type': 'application/json'})
    print("done." if response.ok else "FAILED")

def createIndexAlias():
    print('Creating index alias...')
    url = '{}_aliases'.format(elasticsearch_url)
    data = {
        "actions" : [
            { "add" : { "index" : "{}-000001".format(index), "alias" : index, "is_write_index" : True } }
        ]
    }

    response = requests.post(url, json=data, headers={'Content-type': 'application/json'})
    print("done." if response.ok else "FAILED")

def createIndexLifecyclePolicy():
    print('Creating index lifecycle policy...')
    url = '{}_ilm/policy/{}-policy'.format(elasticsearch_url, index)
    data = {
        "policy": {
            "phases": {
            "warm": {
                "min_age": "10d",
                "actions": {
                "forcemerge": {
                    "max_num_segments": 1
                }
                }
            },
            "delete": {
                "min_age": "30d",
                "actions": {
                "delete": {}
                }
            }
            }
        }
    }

    response = requests.put(url, json=data, headers={'Content-type': 'application/json'})
    print("done." if response.ok else "FAILED")

createIndexTemplate()
createIndex()
createIndexAlias()
createIndexLifecyclePolicy()