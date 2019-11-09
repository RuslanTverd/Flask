from flask import Blueprint
from flask import render_template

tabl = Blueprint('tabl', __name__, template_folder='templates')

@tabl.route('/')
def index():
	return render_template('tabl/index.html')