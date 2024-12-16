from flask import Blueprint, render_template

mechanic_bp = Blueprint('mechanic_bp', __name__)

@mechanic_bp.route('/mechanic_list', methods=['GET', 'POST'])
def mechanics():
    return render_template('mechanic_list.html')