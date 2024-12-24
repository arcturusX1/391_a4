"""
registers blueprints after importing. call from app.py
"""
def register_bp(app):
    from blueprints.home import home_bp
    from blueprints.book_mechanic import book_mechanic_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(book_mechanic_bp)