from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy


from config import Config

db = SQLAlchemy()
bootstrap = Bootstrap()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    bootstrap.init_app(app)

    import loglist
    app.register_blueprint(loglist.bp)
    app.add_url_rule('/', endpoint='loglist.index')

    return app
