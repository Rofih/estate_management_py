import datetime
from dataclasses import dataclass, asdict

from bson import ObjectId


@dataclass
class VisitorPass:
    residentId:str
    time_of_entry: datetime = datetime.datetime.now()
    check_out_time:str = None
    address_visiting:str = None
    pass_id:str = None

    def to_dict(self):
        new_dict = asdict(self)
        if self.pass_id:
            new_dict['pass_id'] = ObjectId(self.pass_id)
        del new_dict['pass_id']
        return new_dict
