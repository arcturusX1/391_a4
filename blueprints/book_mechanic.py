from flask import Blueprint, render_template, redirect, url_for, flash
from blueprints.forms import UserForm
home_bp = Blueprint('home_bp', __name__)

book_mechanic_bp = Blueprint('book_mechanic_bp', __name__)
@book_mechanic_bp.route('/book_mechanic/<int:id>', methods=['GET', 'POST'])
def home():
    form = UserForm()
    return render_template('book_mechanic.html', form=form, mechanic_id = id)