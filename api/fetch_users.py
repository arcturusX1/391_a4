from flask_restful import Resource
from model.database import User

class UserResource(Resource):
    def get(self, user_id=None):
        if user_id:
            user = User.query.get(user_id)
            return{'id': user.id, 'first_name':user.first_name, 'last_name': user.last_name}
        
        users = User.query.all()
        return [{'id': user.id, 'first_name':user.first_name, 'last_name': user.last_name} for user in users]