import os

from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

from myweatherapp.views import blueprint as main_blueprint

app = Flask(__name__)

def create_app():
    """Application creation factory."""


    # Config
    app._static_folder = 'static'
    app.config.update(
        CFG_SITE_NAME='myweatherapp',
    )
    app.config.from_pyfile('config.py', silent=True)


    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404


    @app.context_processor
    def override_url_for():
        return dict(url_for=dated_url_for)


    def dated_url_for(endpoint, **values):
        if endpoint == 'static':
            filename = values.get('filename', None)
            if filename:
                file_path = os.path.join(app.root_path, endpoint, filename)
                values['q'] = int(os.stat(file_path).st_mtime)
        return url_for(endpoint, **values)


    # DB
    if 'SQLALCHEMY_DATABASE_URI' not in app.config:
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

    db = SQLAlchemy(app)
    db.init_app(app)

    # Blueprints
    app.register_blueprint(main_blueprint)

    return app
