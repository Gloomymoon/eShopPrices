import os

from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from flask import Flask, app
from flask_apscheduler import APScheduler
from flask_bootstrap import Bootstrap
#from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from config import config

db = SQLAlchemy()
bootstrap = Bootstrap()

#login_manager = LoginManager()
#login_manager.session_protection = 'strong'
#login_manager.login_view = 'main.login'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    db.app = app
    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #prevent Jobs get scheduled twice: https://github.com/viniciuschiele/flask-apscheduler/issues/58
    if not app.debug or os.environ.get("WERKZEUG_RUN_MAIN") == "true":
        scheduler = APScheduler()
        scheduler.init_app(app)
        scheduler.start()

    return app

