from os import write
import ijson
from elasticsearch import Elasticsearch
import csv

es = Elasticsearch()

index_name = 'tele'
file_path = './../data/data.json'
result_file = './../data/freq.csv'
header = ['title' , 'id', 'news_count']

res = es.search(index=index_name, body={
        "size" : 0,
        "aggs": {
            "channels" : {
                "terms" : {
                    "field": "sender_id",
                    "size" : 100000
                }
            }
        }
    }
)

buckets = res["aggregations"]["channels"]["buckets"]

channels_freq = {}

for bucket in buckets:
    if(channels_freq.get(bucket["key"])):
        print(f'{bucket["key"]} is duplicated ')
    channels_freq[bucket["key"]] = bucket["doc_count"]


f = open(file_path)
csv_file = open(result_file,'w',  encoding='utf-8')
writer = csv.writer(csv_file)
writer.writerow(header)
channels = ijson.items(f, 'channels.item')
for i, channel in enumerate(channels):
    if(channels_freq[channel['id']]):
        print(channel['title'])
        data = [channel['title'], channel['id'],channels_freq[channel['id']]]
        writer.writerow(data)
    else:
        print('invalid id ')

f.close()
csv_file.close()