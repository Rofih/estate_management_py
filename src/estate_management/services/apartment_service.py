from flask import jsonify

from estate_management.data.models.apartment import Apartment
from estate_management.data.repositries.apartment_repository import ApartmentRepository


class ApartmentService:
    def __init__(self):
        self.repository = ApartmentRepository()

    def create_apartment(self, apartment_address):
        apartment = Apartment(apartment_address=apartment_address)
        new_id = self.repository.create_apartment(apartment)
        found_apartment = self.repository.get_apartment_by_id(new_id.apartment_id)
        if found_apartment:
            found_apartment['id'] = str(found_apartment['_id'])
        del found_apartment['_id']
        return found_apartment
    def number_of_apartments(self):
        return len(self.repository.get_apartments())


