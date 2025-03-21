from flask import request, Flask

from estate_management.services.user_service import UserService
app = Flask(__name__)

service = UserService()
@app.route('/register', methods=['POST'])
def sign_up():
    data = request.json
    message = service.create_user(name=data['name'] ,password=data['password'],email=data['email'],role=data['role'])
    return message

@app.route('/login', methods=['POST'])
def log_in():
    data = request.json
    message = service.login_user(email=data['email'],password=data['password'])
    return message

@app.route('/otp', methods=['POST'])
def generate_otp():
    data = request.json
    message = service.generate_token(user_id=data['user_id'])
    return message

@app.route('/assign', methods=['POST'])
def assign_apartment():
    data = request.json
    message = service.assign_apartment_to_resident(resident_id=data['resident_id'],apartment_id=data['apartment_id'],admin_id=data['admin_id'])
    return message

@app.route('/validate_otp', methods=['POST'])
def validate_token():
    data = request.json
    message = service.validate_token(user_id=data['user_id'],security_id=data['security_id'],otp=data['otp'],address=data['address'])
    return message



if __name__ == '__main__':
    app.run(debug=True)