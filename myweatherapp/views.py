from flask import Blueprint, abort, current_app, render_template, request
from jinja2 import TemplateNotFound

from myweatherapp.location.api import LocationResolver
from myweatherapp.location.error import NotFoundLocationError
from myweatherapp.error import BadRequestError

blueprint = Blueprint(
    'myweatherapp_web',
    __name__,
    template_folder='templates',
    static_folder='static'
)


@blueprint.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404


@blueprint.errorhandler(NotFoundLocationError)
def page_location_not_found(e):
    return render_template(
        'errors/not_found_location.html', error_msg=e.msg), 404


@blueprint.errorhandler(BadRequestError)
def page_location_not_found(e):
    return render_template('errors/error.html', error_msg=e.msg), 404


@blueprint.route('/')
def home():
    current_ip = current_app.config['TEST_IP'] if \
        current_app.config['DEBUG'] else request.remote_addr

    location = LocationResolver.resolve(current_ip)
    try:
        return render_template(
            'index.html', location=location, current_ip=current_ip
        )
    except TemplateNotFound:
        abort(404)
