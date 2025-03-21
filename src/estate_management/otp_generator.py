import uuid
class CreateOtp:
    @staticmethod
    def generate_otp():
      new_id = str(uuid.uuid4())
      return new_id[:8]