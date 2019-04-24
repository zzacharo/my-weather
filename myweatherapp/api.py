from flask import Blueprint, abort, current_app, jsonify, request
from jinja2 import TemplateNotFound

from myweatherapp.error import BadRequestError
from myweatherapp.location.api import LocationResolver
from myweatherapp.location.error import NotFoundLocationError
from myweatherapp.weather.api import WeatherResolver
from myweatherapp.weather.error import NotFoundWeatherError

api_blueprint = Blueprint(
    'myweatherapp_rest',
    __name__
)


def serialize_error(error):
    return {
        "message": error.msg
    }


def make_response(body, status_code):
    """."""
    response = jsonify(body)
    response.status_code = status_code
    return response


@api_blueprint.route('/weather')
def index():
    current_ip = current_app.config['TEST_IP'] if \
        current_app.config['DEBUG'] else request.remote_addr
    try:
        weather = WeatherResolver().resolve(current_ip)
    except (BadRequestError, NotFoundLocationError, NotFoundWeatherError) as e:
        return make_response(serialize_error(e), e.code)
    return make_response(weather, 200)
