from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate 

db = SQLAlchemy()
migrate = Migrate()

def create_app(test_config=None):
    app = Flask(__name__)

    #hide a warning about a feature in SQLAlchemy that we won't be using
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    #set app.config['SQLALCHEMY_DATABASE_URI'] to the connection string for our database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/solar_system_development'

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes import planets_bp
    app.register_blueprint(planets_bp)
    
    from app.models.planet import Planet
    
    return app
