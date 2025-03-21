from dataclasses import dataclass, asdict
from bson import ObjectId

from estate_management.data.models.enums import Role


@dataclass
class User:
    name: str
    email: str
    password: str
    role: Role
    id: str = None
    address: str = None

    def __post_init__(self):
        if self.id and isinstance(self.id, ObjectId):
            self.id = str(self.id)

    def to_dict(self):
        user_dict = asdict(self)
        if self.id:
            user_dict['_id'] = ObjectId(self.id)
        del user_dict['id']
        return user_dict