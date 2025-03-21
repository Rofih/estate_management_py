from bson import ObjectId
from pymongo import MongoClient

from estate_management.data.models.user import User


class UserRepository:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['Estate_manager']
        self.collection = self.db['users']

    def create_user(self, user):
        user_dict = user.to_dict()
        return self.collection.insert_one(user_dict).inserted_id

    def find_by_id(self, user_id):
        global new_result
        result =  self.collection.find_one({'_id': ObjectId(user_id)})
        if result:
            if '_id' in result:
                new_result = {
                    'id': str(result['_id']),
                    'name': result['name'],
                    'email': result['email'],
                    'password': result['password'],
                    'role': result['role'],
                    'address': result['address'],
                }
        return User(**new_result)if new_result else None

    def find_by_email(self, email):
        result = self.collection.find_one({'email': email})
        new_result = {
            'id': ObjectId(result['_id']),
            'name':result['name'],
            'email':result['email'],
            'password':result['password'],
            'role':result['role'],
            'address':result['address'],

        }
        return User(**new_result)if new_result else None

    def delete_by_id(self, user_id):
        return self.collection.delete_one({'_id': ObjectId(user_id)}).deleted_count

    def update_user(self, user_id, user):
        user_dict = user.to_dict()
        return self.collection.update_one({'_id': ObjectId(user_id)}, {'$set': user_dict})
