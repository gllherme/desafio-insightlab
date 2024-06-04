from pymongo import MongoClient

client = MongoClient("mongodb://root:example@localhost:27017/")

db = client["database"]

users_collection = db["users"]
