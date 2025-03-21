from bson import ObjectId
from pymongo import MongoClient


class TokenRepository:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['Estate_manager']
        self.collection = self.db['tokens']

    def save(self, token):
        new_token = token.to_dict()
        return self.collection.insert_one(new_token).inserted_id

    def get_by_id(self, token_id):
        return self.collection.find_one({'_id': ObjectId(token_id)})

    def delete_by_id(self, token_id):
        return self.collection.delete_one({'_id': ObjectId(token_id)}).acknowledged

    def get_tokens(self):
        return self.collection.find()




