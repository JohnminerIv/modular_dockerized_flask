from pymongo import MongoClient
import os

client = MongoClient(host=os.getenv("MONGODBURI"))
db = client.get_default_database()