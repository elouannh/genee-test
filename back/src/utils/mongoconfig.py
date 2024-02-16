from pymongo import MongoClient
import re

def connect_client(config):
    """
    The function that starts the mongoDb database system
    """
    print(config.MONGO_USER, config.MONGO_PASS)
    client = MongoClient(host="mongodb://mongo:27017", username=config.MONGO_USER, password=config.MONGO_PASS)

    return client


def split_on_semicolon(s):
    return re.split(';+', s)


def scrap_csv(client):
    db = client['refer']
    col = db['values']

    with open("./src/res/referentiel.csv", "r") as csv:

        columns = split_on_semicolon(csv.readline())

        i = 0
        for line in csv:
            if i == 0:
                i += 1
                continue
            line_content = split_on_semicolon(line)
            dict = {}

            for i in range(len(columns)):
                if i >= len(line_content):
                    dict[columns[i]] = ""
                else:
                    dict[columns[i]] = line_content[i]

            col.insert_one(dict)

