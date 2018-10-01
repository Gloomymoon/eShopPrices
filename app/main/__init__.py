from flask import Blueprint, current_app

main = Blueprint('main', __name__)

from . import views, errors

@main.app_context_processor
def inject_current_app():
    return dict(current_app=current_app)