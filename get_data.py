from pymongo import MongoClient

from scrapy_movies.settings import MONGODB_COLLECTION, MONGODB_HOST, MONGODB_DB, MONGODB_PORT

connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
db = connection[MONGODB_DB]
collection = db[MONGODB_COLLECTION]

print(collection.count())

query = {}
list_results = collection.find(query).limit(100)
list_results = list(list_results)
for i in list_results:
    print(i)
