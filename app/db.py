"""
Database module for the Simple Notes App.

Provides function for connecting to the SQLite database, initializing it, 
and performing basic operations
"""

import sqlite3
import click
from flask import current_app, g

def get_db():
    """
    Establish and return a connection to the SQLite database.

    Returns:
        sqlite3.Connection: The database connection.
    """
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    """
    Close the database connection if it exists.
    """
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    """
    Initialize the database by creating the 'notes' table.
    """
    db = get_db()
    db.executescript("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL
        );
    """)
    db.commit()

def init_app(app):
    """
    Register database functions with the Flask app.

    Args:
        app (Flask): The Flask application instance.
    """
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

@click.command('init-db')
def init_db_command():
    """
    Command to initialize the database.
    """
    init_db()
    click.echo('Initialized the database.')