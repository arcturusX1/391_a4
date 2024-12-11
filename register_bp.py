def register_bp(app):
    from blueprints.home import home_bp

    app.register_blueprint(home_bp)