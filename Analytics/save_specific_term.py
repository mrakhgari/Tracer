import json
from os import WIFSTOPPED
from elasticsearch import Elasticsearch
# from elasticsearch.client.utils import T
from elasticsearch.helpers import scan
import csv

es = Elasticsearch()
index_name = 'tele'
query = 'کرونا کوید corona Covid کووید Corona covid COVID CORONA كوويد كرونا كويد '

channels_file = './../data/freq.csv'
result_file = './specific_query_news.json'
rows = csv.reader(open(channels_file))


next(rows)

result_news = {"channels": []}


for row in rows:
    temp = {}
    temp["title"] = row[0]
    temp["id"] = row[1]
    temp["messages"] = [] 
    print(row[0])
        
    for hit in scan(es, index = index_name, query={
            "query": {
            "bool" : {
                "must" : [
                    {
                        "match": {
                            "message" : query
                        }
                    },
                    {
                        "match" : {
                            "sender_id" : row[1] 
                        }
                    }
                ]
            }   
        }    
    }):
        source = hit["_source"]
        temp["messages"].append({
            "message": source["message"],
            "id":hit["_id"]
        })

    result_news["channels"].append(temp)

with open(result_file, 'w', encoding='utf-8') as f:
    json.dump(result_news, f, ensure_ascii=False, indent=4)