from elasticsearch import Elasticsearch
import csv

query = 'کرونا کوید corona Covid کووید Corona covid COVID CORONA كوويد كرونا كويد '
index_name = 'tele'
channels_file = './../data/freq.csv'
term_freq_file = './../data/term_freq.csv'
all = [] 
writer = csv.writer(open(term_freq_file, 'w', encoding='utf-8'))

rows = csv.reader(open(channels_file, 'r', encoding='utf-8'))
first_row = next(rows)
first_row.append(query)
all.append(first_row)
es = Elasticsearch()

for row in rows:
    print(row[0], row[1])
    result = es.search(index=index_name, body={
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
    })
    count = result['hits']['total']['value']
    row.append(count)
    all.append(row)

writer.writerows(all)


    