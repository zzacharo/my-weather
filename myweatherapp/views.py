from flask import Blueprint, abort, current_app, render_template, request
from jinja2 import TemplateNotFound

blueprint = Blueprint(
    'myweatherapp_web',
    __name__,
    template_folder='templates',
    static_folder='static'
)


@blueprint.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@blueprint.route('/')
def home():
    current_ip = current_app.config['TEST_IP'] if \
        current_app.config['DEBUG'] else request.remote_addr
    try:
        return render_template(
            'index.html', current_ip=current_ip
        )
    except TemplateNotFound:
        abort(404)
