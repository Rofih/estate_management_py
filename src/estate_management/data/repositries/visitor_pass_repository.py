from bson import ObjectId
from pymongo import MongoClient


class VisitorPassRepo:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['Estate_manager']
        self.collection = self.db['visitor_log']

    def create_pass(self, data):
        data_dict = data.to_dict()
        return self.collection.insert_one(data_dict).inserted_id

    def get_visitor_pass(self, pass_id):
        return self.collection.find_one({'_id': ObjectId(pass_id)})

    def delete_visitor_pass_by_id(self, pass_id):
        return self.collection.delete_one({'_id': ObjectId(pass_id)})

    def update_visitor_pass_by_id(self, pass_id, data):
        return self.collection.update_one({'_id': ObjectId(pass_id)}, {'$set': data})