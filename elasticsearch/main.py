from elasticsearch import Elasticsearch
import ijson

es = Elasticsearch()
file_path = './data/data.json'
index_name = 'tele'


f = open(file_path)

# change the second parameter by structure of json
messages = ijson.items(f, 'channels.item.messages.item')
for i, message in enumerate(messages):
    print(i)
    es.index(index=index_name,doc_type='external',body=message, id=i)

