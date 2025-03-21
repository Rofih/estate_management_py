import datetime

import schedule
from flask import jsonify

from estate_management.data.models.token import Token
from estate_management.data.repositries.token_repository import TokenRepository


class TokenService:
    def __init__(self):
        self.token_repository = TokenRepository()


    def create_token(self):
        token = Token()
        new_token = self.token_repository.save(token)
        found_token = self.token_repository.get_by_id(new_token)
        if found_token:
            found_token['id'] = str(found_token['_id'])
        del found_token['_id']
        return found_token

    def get_token(self, token_id):
        new_token = self.token_repository.get_by_id(token_id)
        return jsonify({'token': new_token}),200

    def delete_token(self, token_id):
        status = self.token_repository.delete_by_id(token_id)
        if status:
            return jsonify({'status': 'token deleted'}),200
        else:
            return jsonify({'status': 'process for token deletion failed'}),401

    def number_of_tokens(self):
        return len(self.token_repository.get_tokens())


    def delete_crawler(self):
        tokens = self.token_repository.get_tokens()
        for token in tokens:
            if datetime.datetime.now() >= token.expiration_time:
                self.token_repository.delete_by_id(token.id)
                print(f'i just deleted this token{token.id}')

        print('i am checking')

    schedule.every(10).minutes.do(delete_crawler)
