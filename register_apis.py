from config import api
#Import api modules here
from api.fetch_users import UserResource
from api.mechanics_resource import MechanicResource


def register_apis():
    api.add_resource(UserResource, '/api/users')
    api.add_resource(MechanicResource, '/api/mechanics')