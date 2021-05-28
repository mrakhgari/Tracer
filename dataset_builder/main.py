from elasticsearch import Elasticsearch
import json

es = Elasticsearch()

index_name = 'tele'
file_path = './../data/result.json'

f = open(file_path, 'r+', encoding='utf-8')
j = json.load(f)
json_file = j["messages"]


def get_json_format(hit):
    _source = hit["_source"]
    _id = hit["_id"]

    print(f'message:\n {_source["message"]}')
    if input("you want to add it? (N for no)\n").upper() != "N":
        return True, {
            "_id": _id,
            "message": _source["message"]
        }
    return False, None


def get_replied_message(_id, _sender_id, messages):
    res = es.search(index=index_name, body={
        "query": {
            "bool": {
                "must": [
                    {
                        "match": {
                            "id": _id
                        }
                    },
                    {
                        "match": {
                            "sender_id": _sender_id
                        }
                    }
                ]
            }
        }})
    m = {}
    for hit in res['hits']['hits']:
        valid_message, message = get_json_format(hit)
        if valid_message:
            m = hit
            messages.append(message)
    return m


while True:
    title = input("Enter the title: \n")
    query = input("Enter the query: \n")
    if not query:
        break

    res = es.search(index=index_name, body={
        "query": {
            "bool": {
                "must": {
                    "match": {
                        "message": query
                    }
                },
                "must_not": {
                    "match": {
                        "message": "کذب شایعه تکذیب"
                    }
                }
            }
        }
    })
    messages = []
    for hit in res['hits']['hits']:
        _source = hit["_source"]
        valid_message, message = get_json_format(hit)

        if valid_message:
            messages.append(message)
            if _source["reply_to"]:
                m = _source
                while(m.get("reply_to")):
                    print("========={replid message}===========\n\n")
                    m = get_replied_message(
                        m["reply_to"]["reply_to_msg_id"], _source["sender_id"], messages)
                    if (m.get("_source")):
                        m = m["_source"]

    json_file.append({
        "title": title,
        "query": query,
        "messages": messages
    })

f.seek(0)
json.dump(j, f, ensure_ascii=False)

f.close()
