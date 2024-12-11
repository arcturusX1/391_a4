from flask import Flask, redirect, url_for
from register_bp import register_bp
app = Flask(__name__)

register_bp(app)





if __name__=="__main__":
    app.run(host='0.0.0.0', debug=True)