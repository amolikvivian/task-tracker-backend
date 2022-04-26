from dotenv import dotenv_values
from pymongo import MongoClient

config = dotenv_values(".env") 

client = MongoClient(config['MONGO_URI'])
db_name = config["DB_NAME"]

db = client[db_name]