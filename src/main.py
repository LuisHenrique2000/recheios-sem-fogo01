from flask import Flask
from src.routes.public import public_bp
from src.routes.admin import admin_bp
from src.db import Base, engine  # <-- IMPORTANTE: conexão com banco

def create_app():
    app = Flask(_name_)
    app.config["SECRET_KEY"] = "trocar-por-chave-segura"

    app.register_blueprint(public_bp)
    app.register_blueprint(admin_bp)

    Base.metadata.create_all(bind=engine)  # <-- CRIA AS TABELAS

    return app
