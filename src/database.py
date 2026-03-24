import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect("results.db")
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS runs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT,
            transcription TEXT,
            cleaned_text TEXT,
            accuracy REAL,
            timestamp TEXT
        )
    ''')

    conn.commit()
    conn.close()


def save_run(filename, transcription, cleaned_text, accuracy):
    conn = sqlite3.connect("results.db")
    c = conn.cursor()

    c.execute('''
        INSERT INTO runs (filename, transcription, cleaned_text, accuracy, timestamp)
        VALUES (?, ?, ?, ?, ?)
    ''', (filename, transcription, cleaned_text, accuracy, datetime.now()))

    conn.commit()
    conn.close()