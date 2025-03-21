from flask import Flask, request, jsonify

from estate_management.services.apartment_service import ApartmentService

app = Flask(__name__)

service = ApartmentService()

@app.route('/create_apartment', methods=['POST'])
def create_apartment():
    data = request.json
    message = service.create_apartment(apartment_address=data['apartment_address'])
    # print(message)
    return jsonify(message),201


if __name__ == '__main__':
    app.run(debug=True)