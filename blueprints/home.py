from flask import Blueprint, render_template, redirect, url_for, flash
from blueprints.forms import UserForm
from model.database import db
home_bp = Blueprint('home_bp', __name__)

@home_bp.route('/')
def home():
    form = UserForm()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
    
    try:
        db.session.add.User(first_name=first_name, last_name=last_name)
        db.session.commit()
        flash("added")
    except Exception as e:
        db.session.rollback()
        flash(f"error: {e}")
        
    
    return render_template('index.html', form=form)