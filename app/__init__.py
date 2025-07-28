# app/__init__.py

from flask import Flask
from markupsafe import Markup
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import markdown  #  Import Markdown library
from config import Config

# Initialize extensions (without app for now)
db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'main.login'  # Redirect to login page if user not logged in

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions with app
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

    # Register blueprints (routes grouped together)
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Markdown filter for Jinja2 templates
    @app.template_filter('markdown')
    def markdown_filter(text):
        # Convert Markdown to HTML safely
        return Markup(markdown.markdown(text, extensions=["fenced_code"]))

    return app
