"""
initializes configurations. import into app.py and call. 
"""

import os 

from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from model.database import db


class Config:
    SQLALCHEMY_DATABASE_URI = os.environ['URI']
    SECRET_KEY = os.environ['SECRET_KEY']


def init_app(app):
    app.config.from_object(Config)
    migrate = Migrate()
    csrf  = CSRFProtect()
    db.init_app(app)
    migrate.init_app(app)
    csrf.init_app(app)

    with app.app_context():
        db.create_all()

    import logging
    logging.basicConfig(level=logging.DEBUG)

    return app