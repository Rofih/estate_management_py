from flask import jsonify

from estate_management.data.models.visitor_pass import VisitorPass
from estate_management.data.repositries.visitor_pass_repository import VisitorPassRepo


class VisitorPassService:
    def __init__(self):
        self.pass_repository = VisitorPassRepo()

    def create_visitor_pass(self,user_id,address):
        new_pass = VisitorPass(residentId=user_id,address_visiting=address)
        new_id = self.pass_repository.create_pass(new_pass)
        return jsonify({'pass_id':new_id,'message':'created successfully!'})

    def update_visitor_pass(self,pass_id,check_out_time):
        new_pass = self.pass_repository.get_visitor_pass(pass_id)
        new_pass.check_out_time = check_out_time
        self.pass_repository.update_visitor_pass_by_id(pass_id,new_pass)
        return jsonify({'pass':new_pass.to_dict(),'message':'updated successfully!'})