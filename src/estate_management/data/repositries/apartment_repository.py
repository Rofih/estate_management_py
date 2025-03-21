from bson import ObjectId
from pymongo import MongoClient

from estate_management.data.models.apartment import Apartment


class ApartmentRepository:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['Estate_manager']
        self.collection = self.db['apartments']

    def create_apartment(self, apartment):
        new_apartment = apartment.to_dict()
        result = self.collection.insert_one(new_apartment).inserted_id
        created_apartment = self.collection.find_one({"_id": result})
        return Apartment.from_dict(created_apartment) if created_apartment else None

    def get_apartments(self):
        return self.collection.find()

    def get_apartment_by_id(self, apartment_id):
        return self.collection.find_one({'_id': ObjectId(apartment_id)})

    def delete_apartment(self, apartment_id):
        return self.collection.delete_one({'_id': ObjectId(apartment_id)})

    def update_apartment(self, apartment_id, apartment):
        return self.collection.update_one({'_id': ObjectId(apartment_id)},apartment)
