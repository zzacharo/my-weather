from flask import Blueprint, abort, current_app, render_template, request
from jinja2 import TemplateNotFound


ui_blueprint = Blueprint(
    'myweatherapp_ui',
    __name__,
    template_folder='templates',
    static_folder='static'
)


@ui_blueprint.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404


@ui_blueprint.route('/')
def home():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)
