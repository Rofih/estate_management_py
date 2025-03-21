from dataclasses import dataclass

from bson import ObjectId

@dataclass
class Apartment():
    apartment_address:str
    apartment_owner:str = None
    apartment_id:str = None


    def to_dict(self):
        new_dict = {
            'apartment_id':None,
            'apartment_address': self.apartment_address,
            'apartment_owner': self.apartment_owner
        }
        if self.apartment_id :
            new_dict['_id'] = ObjectId(self.apartment_id)
        del new_dict['apartment_id']
        return new_dict

    def __post_init__(self):
        if self.apartment_id and isinstance(self.apartment_id, ObjectId):
            self.apartment_id = str(self.apartment_id)

    @staticmethod
    def from_dict(data):
        apartment_id = str(data.get('_id')) if data.get('_id') else None
        return Apartment(
            apartment_address=data['apartment_address'],
            apartment_owner=data.get('apartment_owner'),
            apartment_id=apartment_id
        )