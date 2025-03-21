import uuid
class CreateId:

    def generateId(self):
      new_id = str(uuid.uuid4())
      return new_id[:8]