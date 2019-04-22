import os

from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# Extensions registration
db = SQLAlchemy(app)

def create_app():
    """Application creation factory."""
    from myweatherapp.views import blueprint as main_blueprint


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

    # Blueprints
    app.register_blueprint(main_blueprint)

    return app
