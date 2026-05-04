import sqlite3
from flask import g
from config.config import DATABASE

def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

def close_db(e=None):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()

def init_db(app):
    with app.app_context():
        db = get_db()
        cursor = db.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        """)

        db.commit()