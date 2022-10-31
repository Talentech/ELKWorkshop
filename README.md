# Eleasticsearch/Kibana workshop

## Playground setup
1. Install docker:
   - **Windows**: Install *Docker for Windows* **with WSL2 backend** from [here](https://docs.docker.com/desktop/install/windows-install/)
   - **Linux**: Install using apt-get or any other package manager according to [this](https://docs.docker.com/engine/install/) instruction
    
1. Open terminal/shell
1. Go to playground folder
1. Run command:
    ```
    docker-compose up
    ```
1. After containers spinup you should be able to access:
    - [ElasticSearch](http://localhost:9200/)
    - [Kibana](http://localhost:5601)


## Lessons

### Lesson 1 - Setting up new index with lifecycle policy

**DON'T CREATE INDICES PER DAY/MONTH/YEAR - it's simply waste of resources!!!**
Create indices with index lifecycle instead. So assuming that your indes is called `my-index`:
1. Open [Kibana](http://localhost:5601)
1. Go to [DevTools](http://localhost:5601/app/kibana#/dev_tools/) in Kibana navigation panel - this tool will allow you to send REST requests to ElasticSearch
1. Create index template:
    ```
    PUT _template/my-index_template
    {
        "index_patterns": ["my-index*"],                 
        "settings": {
            "number_of_shards": 3,
            "number_of_replicas": 1,
            "index.lifecycle.name": "my-index-policy",      
            "index.lifecycle.rollover_alias": "my-index"    
        }
    }
    ```
1. Create index:
    ```
    PUT /my-index-000001
    {
        "settings": {
            "index": {
            "number_of_shards": 3,  
            "number_of_replicas": 2 
            }
        }
    }
    ```
1. Create index alias by sending following request in DevTools console:
    ```
    POST /_aliases
    {
        "actions" : [
            { "add" : { "index" : "my-index-000001", "alias" : "my-index", "is_write_index" : true } }
        ]
    }
    ```
1. Go to your new `my-index-000001` settings via Kibana ([Management -> Index Management](http://localhost:5601/app/kibana#/management/elasticsearch/index_management/) -> select `my-index-000001` from the list -> switch to "Edit settings" tab and ensure that there are following entries:
    ```
    ...
    "settings": {
        ...
        "index.lifecycle.name": "my-index-policy",
        "index.lifecycle.rollover_alias": "my-index"
        ...
    }
    ...
    ```
    or
    ```
    ...
    "settings": {
        ...
        "index": {
            "lifecycle": {
                "name": "talmundo-logs-policy",
                "rollover_alias": "talmundo-logs"
            }
            ...
        }
        ...
    }
    ```

1. Go to [Management -> Index Lifecycle Policies](http://localhost:5601/app/kibana#/management/elasticsearch/index_lifecycle_management/policies?_g=()) and click *Create Policy* button.

1. Configure your policy. **It's important to put policy name the same as in the configuration above** - so in this case `my-index-policy`.


Reference: https://www.elastic.co/guide/en/elasticsearch/reference/7.6/getting-started-index-lifecycle-management.html



