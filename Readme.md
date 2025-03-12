# Simple Notes App

## Overview

Simple Notes App is a minimal web application for taking short text notes. Users can add new notes and delete existing ones. The app is built with Python and Flask and uses SQLite for storing notes.

## Features

- **Add Notes:** Submit short text notes via a web form.
- **Delete Notes:** Remove notes with a single click.
- **View Notes:** See a list of all saved notes.

## Project Structure

simple-notes-app/
├── app/
│   ├── __init__.py       # Application factory and configuration.
│   ├── db.py             # Database connection and operations.
│   └── routes.py         # Web routes for handling note requests.
├── templates/
│   ├── base.html         # Base HTML template.
│   └── index.html        # Main page template for listing and adding notes.
├── tests/
│   └── test_app.py       # Unit tests for the application.
├── requirements.txt      # Project dependencies.
├── README.md             # Project documentation.
└── Dockerfile            # Containerization instructions.


## Installation

1. **Clone the repository:**

   git clone https://github.com/sumanth-s-code/notes-app.git
   cd simple-notes-app

2. **Create and activate a virtual environment (optional but recommended):**

    python3 -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate

3. **Install dependencies:**

    pip install -r requirements.txt



