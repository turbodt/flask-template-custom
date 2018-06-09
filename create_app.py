import os
from flask import Flask

from .config import Configuration
from . import models, routes, socketio

from flask_sslify import SSLify

def create_app(config_name):
    print('create_app.py create_app(config_name)')

    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY='mysecretkey',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    app.config.from_object(Configuration(config_name))

    if app.config['HTTPS_REQUIRED']:
        sslify = SSLify(app)

    models.init_app(app)
    routes.init_app(app)
    socketio.init_app(app)

    return app
