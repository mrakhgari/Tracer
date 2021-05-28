from os import write
import ijson
import csv

file_path = './../data/result.json'

header = ['title', 'query', 'id', 'message', 'label']

f = open(file_path)
messages = ijson.items(f, 'messages.item')


def get_label(label: str):
    if label == "F":
        return "fake"
    elif label == "Q":
        return "question"
    elif label == "MI":
        return "moreinfo"
    elif label == "D":
        return "denial"
    elif label == "I":
        return "irrelevant"
    else:
        return "unlabeled"


with open('./../data/labeled.csv', 'w', encoding='utf8') as labeld_file:
    writer = csv.writer(labeld_file)
    writer.writerow(header)
    for i, news in enumerate(messages):
        title = news["title"]
        query = news["query"]
        print("Title is")
        print(title)
        for message in news["messages"]:
            print('message is ============================================== ')
            print(message["message"])
            label = get_label(input(
                "Enter the label(f or F: fake, q:question, mi:moreinfo, d:denial, i:irrelevant) ").upper())
            data = [title, query, message["_id"], message["message"], label]
            writer.writerow(data)
