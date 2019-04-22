import json

import pytest
from flask import url_for
from myweatherapp.factory import create_app, db


@pytest.fixture()
def app():
    """Flask application fixture."""
    app_ = create_app()
    db.create_all()
    app_.config['SERVER_NAME'] = 'localhost:5000'
    with app_.app_context():
        yield app_
    db.drop_all()
