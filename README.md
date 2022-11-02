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

1. Install python 3 - it will be necessary to run some examples.

## Lessons
[Lesson 1 - Setting up new index with lifecycle policy](docs/Lesson1_setting_index_lifecycle_policy.md)

[Lesson 2 - Using logger](docs/Lesson2_using_logger.md)

[Lesson 3 - Using ElasticSearch REST API](docs/Lesson3_using_elasticsearch_rest_api.md)

[Lesson 4 - Aggregations](docs/Lesson4_aggregations.md)

[Lesson 5 - Visualizations and Dashboards](docs/Lesson5_visualizations_and_dashboards.md)
