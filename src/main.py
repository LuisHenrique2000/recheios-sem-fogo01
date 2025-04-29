from flask import Flask
from src.routes.public import public_bp
from routes.admin import admin_bp

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "trocar-por-chave-segura"

    app.register_blueprint(public_bp)
    app.register_blueprint(admin_bp)

    return app
