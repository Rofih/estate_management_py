import datetime
from dataclasses import dataclass

from bson import ObjectId

from estate_management.otp_generator import CreateOtp

@dataclass
class Token:
    otp:str = CreateOtp.generate_otp()
    time_created:datetime = datetime.datetime.now()
    expiration_time:datetime = datetime.datetime.now() + datetime.timedelta(hours=1)
    token_id:str = None


    def to_dict(self):
        new_dict = {
            'otp': self.otp,
            'time_created': self.time_created,
            'expiration_time': self.expiration_time
        }
        if self.token_id:
            new_dict['token_id'] = ObjectId(self.token_id)
        # del new_dict['token_id']
        return new_dict