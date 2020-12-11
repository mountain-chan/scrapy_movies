from pymongo import MongoClient
from bson import ObjectId

from scrapy_movies.settings import MONGODB_PORT, MONGODB_COLLECTION, MONGODB_DB, MONGODB_HOST


class ScrapyMoviesPipeline:
    def __init__(self):
        connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
        self.db = connection[MONGODB_DB]
        self.collection = self.db[MONGODB_COLLECTION]

    def process_item(self, item, spider):
        self.collection.insert({"_id": str(ObjectId()),
                                'link_season': item['link_season'][0],
                                'episodes': item['episodes']
                                })
        return item
