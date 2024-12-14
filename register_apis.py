from config import api
#Import api modules here
from api.fetch_users import UserResource

def register_apis():
    api.add_resource(UserResource, '/api/users')