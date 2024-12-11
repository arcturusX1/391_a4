from flask import Flask, redirect, url_for
from register_bp import register_bp
from config import init_app
app = Flask(__name__)

register_bp(app)
init_app(app)

if __name__=="__main__":
    app.run(host='0.0.0.0', debug=True)