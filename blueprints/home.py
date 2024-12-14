from flask import Blueprint, render_template, redirect, url_for, flash
from blueprints.forms import UserForm
from model.database import db, User

home_bp = Blueprint('home_bp', __name__)

@home_bp.route('/', methods=['GET', 'POST'])
def home():
    form = UserForm() 
    return render_template('index.html', form=form)