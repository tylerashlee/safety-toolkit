from flask import Flask
from app.routes import main as main_blueprint  # Correct: importing the actual Blueprint object

def create_app():
    app = Flask(__name__)

    app.register_blueprint(main_blueprint)

    return app

