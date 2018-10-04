#Simple program to create Mongodb database
from pymongo import MongoClient

client = MongoClient()

db = client.TestDB

#Creating a sample collection

family = [
            {'name':'Padma Prakash','age':29,'city':'Chennai'},
            {'name':'Shyni Prakash','age':26,'city':'Chennai'},
            {'name':'Prasanna','age':36,'city':'Atlanta'},
]

myCollection = db.FirstCollection

for f in family:
    myCollection.insert_one(f)