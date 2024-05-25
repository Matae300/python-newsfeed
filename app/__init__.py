import os
from flask import Flask
from app.routes import home, dashboard
from app.utils import filters
from app.db import init_db
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

def create_app(test_config=None):
    # Set up app config
    app = Flask(__name__, static_url_path='/')
    app.url_map.strict_slashes = False
    app.jinja_env.filters['format_url'] = filters.format_url
    app.jinja_env.filters['format_date'] = filters.format_date
    app.jinja_env.filters['format_plural'] = filters.format_plural
    
    # Load default configuration
    app.config.from_mapping(
        SECRET_KEY=os.getenv('SECRET_KEY', 'dev_secret_key')  # Use a default secret key if not set in env
    )

    if test_config is not None:
        # Load the test config if passed in
        app.config.update(test_config)
    
    # Simple route for testing
    @app.route('/hello')
    def hello():
        return 'hello world'
    
    # Register blueprints
    app.register_blueprint(home)
    app.register_blueprint(dashboard)

    # Initialize the database
    init_db(app)

    return app