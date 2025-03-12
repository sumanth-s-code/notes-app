"""
Routes module for the Simple Notes App.

Defines the web routes to display, add, and delete notes.
"""

from flask import Blueprint, render_template, request, redirect, url_for, flash
from .db import get_db

bp = Blueprint('notes', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
    """
    Display all notes and handle note creation.

    - GET: Renders the main page with all notes.
    - POST: Adds a new note to the database.
    """
    db = get_db()
    if request.method == 'POST':
        note_content = request.form.get('content', '').strip()
        if not note_content:
            flash('Note content cannot be empty.', 'error')
        else:
            db.execute('INSERT INTO notes (content) VALUES (?)', (note_content,))
            db.commit()
            flash('Note added successfully!', 'success')
        return redirect(url_for('notes.index'))
    else:
        cur = db.execute('SELECT id, content FROM notes ORDER BY id DESC')
        notes = cur.fetchall()
        return render_template('index.html', notes=notes)

@bp.route('/delete/<int:note_id>', methods=['POST'])
def delete(note_id):
    """
    Delete a note by its ID.

    Args:
        note_id (int): The ID of the note to delete.
    """
    db = get_db()
    db.execute('DELETE FROM notes WHERE id = ?', (note_id,))
    db.commit()
    flash('Note deleted successfully!', 'success')
    return redirect(url_for('notes.index'))