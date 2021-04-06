from flask import (Blueprint, render_template)


bp = Blueprint('landing_page', __name__, template_folder='templates')
@bp.route('/')
def index():
    """Index page of the application"""
    return render_template("landing_page/index.html")