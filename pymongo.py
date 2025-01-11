from pymongo import MongoClient
import json

cluster = MongoClient("mongodb+srv://mongodbtest:%40123456%21%21@cluster0.a1cp8.mongodb.net/test?retryWrites=true&w=majority")

db = cluster["test_database"]  
collection = db["test_collection"] 


with open('data.json', 'r') as f:
    data = json.load(f)


collection.insert_many(data)