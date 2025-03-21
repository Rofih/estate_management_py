from unittest import TestCase

from estate_management.services.token_service import TokenService


class TestTokenService(TestCase):
    token_service = TokenService()
    def test_create_token(self):
        token = self.token_service.create_token()
        print(token)
        expected = 1
        length = self.token_service.number_of_tokens()
        self.assertEqual(expected,length )

    def test_get_token(self):
        self.fail()

    def test_delete_token(self):
        self.fail()

    def test_delete_crawler(self):
        self.fail()
