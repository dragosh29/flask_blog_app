from flask import Flask
from app.extensions import db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        # Importing models here ensures they are registered with SQLAlchemy
        from .models import User, Post
        db.create_all()

        # Register Blueprints
        from .routes import main
        app.register_blueprint(main)

    return app
