#simple program to read data from MongoDB
from pymongo import MongoClient
import pprint

client = MongoClient()

db = client.TestDB

collectionlist = []

for c in db.list_collection_names():
    collectionlist.append(c)


# for c in db.FirstCollection.find():
#     pprint.pprint(c)


for c in db.FirstCollection.find({'name':'Shyni Prakash'}):
    pprint.pprint(c)