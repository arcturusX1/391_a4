from flask import Flask, redirect, url_for
from register_bp import register_bp
from config import init_app
from register_apis import register_apis
app = Flask(__name__)

init_app(app)
register_bp(app)
register_apis()

if __name__=="__main__":
    app.run(host='0.0.0.0', debug=True)