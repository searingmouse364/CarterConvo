from flask import Blueprint
from flask import render_template
from flask import request

views = Blueprint('views', __name__)


## home page
@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template("index.html")