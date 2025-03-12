"""
Flask application factory for the Simple Notes App.

This module creates and configures the Flask app instance.
"""

from flask import Flask
import os

def create_app(test_config=None):
    """Factory to create and configure the Flask app."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',  # Change this in production
        DATABASE=os.path.join(app.instance_path, 'notes.db')
    )

    if test_config:
        app.config.update(test_config)

    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Initialize the database
    from . import db
    db.init_app(app)

    # Register the routes blueprint
    from . import routes
    app.register_blueprint(routes.bp)

    return app