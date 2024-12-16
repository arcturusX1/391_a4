"""
registers blueprints after importing. call from app.py
"""
def register_bp(app):
    from blueprints.home import home_bp
    from blueprints.mechanics import mechanic_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(mechanic_bp)