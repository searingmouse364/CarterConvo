import os
from flask import Flask


def create_app():
    app = Flask(__name__, template_folder="templates")
    app.config['SECRET_KEY'] =  "WDHJKQAWDkajwhdwiouqdyhjakhdw38y3782y1gj" ## to be changed later

    from .views import views


    app.register_blueprint(views, url_prefix='/')

    return app