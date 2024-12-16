from flask_restful import Resource, reqparse
from flask import jsonify, request, flash
from flask_wtf.csrf import validate_csrf
from blueprints.forms import UserForm

from model.database import Mechanic, Appointment

class MechanicResource(Resource):
    def get(self, id=None):
        # If an ID is provided, return mechanic details for that ID
        if id is not None:
            mechanic = Mechanic.query.get(id)  # Query for a specific mechanic
            if not mechanic:
                return {"error": "Mechanic not found"}, 404
            
            return {
                'id': mechanic.id,
                'name': mechanic.name,
                'appt_number': mechanic.appt_number
            }
        # If no ID is provided, return all mechanics
        mechanics = Mechanic.query.all()
        return [
            {
                'id': mechanic.id,
                'name': mechanic.name,
                'appt_number': mechanic.appt_number
            }
            for mechanic in mechanics
        ]







            
            
        
        
