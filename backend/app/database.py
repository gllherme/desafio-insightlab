from pymongo import MongoClient

client = MongoClient("mongodb://root:example@mongo:27017/")
print(client.list_database_names)

db = client["database"]

users_collection = db["users"]
