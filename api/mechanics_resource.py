from flask_restful import Resource, reqparse
from flask import jsonify, request, flash
from flask_wtf.csrf import validate_csrf
from blueprints.forms import UserForm

from model.database import Mechanic, db

class MechanicResource(Resource):
    def get(self):
        mechanics = Mechanic.query.all()
        
        return [{'id': mechanic.id,
                 'name': mechanic.name,
                 'appt_number': mechanic.appt_number
                 } for mechanic in mechanics]