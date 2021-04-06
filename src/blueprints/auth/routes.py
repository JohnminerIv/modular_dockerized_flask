from flask import (Blueprint, render_template)
bp = Blueprint('auth', __name__, url_prefix='/auth', template_folder='templates')

@bp.route('/login')
def login():
    """Page for logging in"""
    return render_template('auth/login.html')

@bp.route('/register')
def register():
    """Page for registering"""
    return render_template('auth/register.html')