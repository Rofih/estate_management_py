from unittest import TestCase

from estate_management.controllers.user_controller import service
from estate_management.services.apartment_service import ApartmentService


class TestApartmentService(TestCase):
    service = ApartmentService()
    def test_that_i_can_create_apartment(self):
        message = self.service.create_apartment('Block 2 Flat B')
        print(message)
        expected = 1
        self.assertEqual(expected,service.number_of_apartments())

