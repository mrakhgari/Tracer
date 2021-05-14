# Elasticsearch

We use `Elasticsearch` and `Kibana` to retrieve the information we crawled from Telegram.

Due to the size of the data, we can not enter the data directly in the elastic search, so we must use `Logstash` or use the programming language to enter the data. Our json was very complicated. So I can not use `Logstash` and write a good filter in the configuration file. So I decided to use Python to import data.

The data file is so large. so we need to read it async. So we use `ijson` library, and for working with Elasticsearch we use the `ElasticSearch` library in Python.


Furthermore, if you have an error running main.py, I suggest using the following command in the terminal:
``` bash

curl -XPUT -H "Content-Type: application/json" http://localhost:9200/_all/_settings -d '{"index.blocks.read_only_allow_delete": null}'
```
- Note: change 9200 with the port of elastic search that you set in config file.


If you have another problem to run this code, just say to [me](mra.akhgari@gmail.com).
