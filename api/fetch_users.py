from flask_restful import Resource, reqparse
from flask import jsonify, request, flash
from flask_wtf.csrf import validate_csrf

from model.database import User, db

class UserResource(Resource):
    def get(self, user_id=None):
        if user_id:
            user = User.query.get(user_id)
            return{'id': user.id, 'first_name':user.first_name, 'last_name': user.last_name}
        
        users = User.query.all()
        return [{'id': user.id, 'first_name':user.first_name, 'last_name': user.last_name} for user in users]

    def post(self):
        #manual CSRF validation
        #data from js comes here. look for csrf token in headers
        csrf = None
        if 'X-CSRFToken' in request.headers:
            csrf = request.headers['X-CSRFToken']
        try:
            validate_csrf(csrf)
        except Exception as e:
            return {'error': 'Invalid CSRF' }, 400
        
        parser = reqparse.RequestParser()
        parser.add_argument('first_name', type=str, required=True)
        parser.add_argument('last_name', type=str, required=True)
        args = parser.parse_args()

        first_name = args['first_name']
        last_name = args['last_name']

        #add data to db
        try:
            db.session.add(User(first_name=first_name, last_name=last_name))
            db.session.commit()
            print(f'added {first_name}{last_name}')
        except Exception as e:
            db.session.rollback()
            print(f"error: {e}")

        return {'message': 'success', 'data': {'first-name': first_name, 'last-name': last_name}}
