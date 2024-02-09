from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:experion%40123@localhost/training"
    app.config["JWT_SECRET_KEY"] = "userpass"

    #Connecting db and configured app
    db.init_app(app)
    jwt = JWTManager(app)

    from app.user import user_bp
    app.register_blueprint(user_bp)
   
    return app

