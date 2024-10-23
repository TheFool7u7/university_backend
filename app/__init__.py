  config.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from .config import Config

# Inicializar la extensión SQLAlchemy
db = SQLAlchemy()

def create_app():
    # Crear la aplicación Flask
    app = Flask(__name__)
    
    # Cargar la configuración
    app.config.from_object(Config)
    
    # Inicializar CORS
    CORS(app)
    
    # Inicializar la base de datos
    db.init_app(app)
    
    # Importar y registrar blueprints
    from .routes import auth, academic, courses, assignments
    app.register_blueprint(auth.bp, url_prefix='/api/auth')
    app.register_blueprint(academic.bp, url_prefix='/api/academic')
    app.register_blueprint(courses.bp, url_prefix='/api/courses')
    app.register_blueprint(assignments.bp, url_prefix='/api/assignments')
    
    return app