from flask import jsonify
from estate_management.data.models.user import User
from estate_management.data.repositries.apartment_repository import ApartmentRepository
from estate_management.data.repositries.token_repository import TokenRepository
from estate_management.data.repositries.user_repository import UserRepository
from estate_management.services.token_service import TokenService
from estate_management.services.visitor_pass_service import VisitorPassService


class UserService:
    def __init__(self):
        self.repository = UserRepository()
        self.apartment_repository = ApartmentRepository()
        self.token_service = TokenService()
        self.token_repository = TokenRepository()
        self.visitor_pass_service = VisitorPassService()

    def create_user(self, name, email, password, role):
        result = self.repository.find_by_email(email)
        if result is not None:
            return jsonify({'message': 'User already exists'}), 400
        user = User(name=name, email=email, password=password, role=role)
        new_id = self.repository.create_user(user)
        return jsonify({'user_id':  str(new_id),'user_name':name,'message':'User created successfully!'}), 201

    def login_user(self, email, password):
        new_user = self.repository.find_by_email(email)
        if new_user is None:
            return jsonify({'message':'User does not exists!'}), 401
        if new_user.password == password:
            return jsonify({'user_id':new_user.id,'user_name':new_user.name,'message':'User logged in successfully!'}), 200
        else:
            return jsonify({'message':'Wrong password!'}), 401


    def generate_token(self,user_id):
        new_user = self.repository.find_by_id(user_id)
        if new_user is None:
            return jsonify({'message':'User does not exists!'}), 401
        if new_user.role != 'RESIDENT':
            return jsonify({'message':'User is not a resident!'}), 401
        else:
            new_token = self.token_service.create_token()
            return jsonify({'token':new_token}), 200

    def assign_apartment_to_resident(self, admin_id, resident_id, apartment_id):
        admin = self.repository.find_by_id(admin_id)
        # print(admin)
        resident = self.repository.find_by_id(resident_id)
        # print(resident)
        apartment = self.apartment_repository.get_apartment_by_id(apartment_id)
        print(apartment)
        if admin.role == 'ADMIN' and resident.role == 'RESIDENT':
            if apartment.apartment_owner is None:
                resident.address = apartment.get('apartment_address')
                self.repository.update_user(resident_id, resident)

                apartment.apartment_owner = resident.get('name')
                self.apartment_repository.update_apartment(apartment_id, apartment)
                return jsonify({'apartment': apartment.to_dict(), 'message': 'assigned successfully!'}), 200
            else:
                return jsonify({'message': 'apartment already have an owner'}), 401

    def validate_token(self,security_id, otp,user_id,address):
        security = self.repository.find_by_id(security_id)
        if security.role != 'SECURITY':
            return jsonify({'message':'User is not a security !'}), 401
        if security is not None:
            tokens = self.token_repository.get_tokens()
            for token in tokens:
                if token.get('otp') == otp:
                    message = self.visitor_pass_service.create_visitor_pass(user_id=user_id,address=address)
                    return message,201
                return jsonify({'message':'visitor pass was not created!'}), 401

        else:
            return jsonify({'message':'user(security) does not exists!'}), 401

