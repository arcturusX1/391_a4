from flask import Blueprint, render_template, redirect, url_for, flash

home_bp = Blueprint('home_bp', __name__)

@home_bp.route('/', methods=['GET', 'POST'])
def home():
    return render_template('mechanic_list.html')