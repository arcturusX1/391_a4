from flask_restful import Resource, reqparse
from flask import jsonify, request, flash
from flask_wtf.csrf import validate_csrf
from blueprints.forms import UserForm

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
        
        # parser = reqparse.RequestParser()
        # parser.add_argument('first_name', type=str, required=True)
        # parser.add_argument('last_name', type=str, required=True)
        # args = parser.parse_args()

        # first_name = args['first_name']
        # last_name = args['last_name']

        form = UserForm(data=request.get_json())

        if not form.validate():
            return {'error': 'Validation error', 'errors': form.errors}, 400
        
        first_name = form.first_name.data
        last_name = form.last_name.data
        address = form.address.data
        phone = form.phone.data
        car_license = form.car_license.data
        car_engine = form.car_engine.data

        #add data to db
        try:
            user = User(first_name=first_name,
                        last_name=last_name,
                        address=address,
                        phone=phone,
                        car_license=car_license,
                        car_engine=car_engine
                        )
            db.session.add(user)
            db.session.commit()
            print(f'added {first_name}{last_name}')
        except Exception as e:
            db.session.rollback()
            print(f"error: {e}")

        return {'message': 'success', 'data': {'first-name': first_name, 'last-name': last_name}}, 201
