import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    database_url = os.environ.get('DATABASE_URL') or 'postgresql://postgres:postgres@db:5432/postgres'
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app
