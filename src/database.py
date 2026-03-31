import sqlite3

DB_PATH = "results.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS runs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT,
        accuracy REAL,
        transcription TEXT,
        cleaned_text TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)
    conn.commit()
    conn.close()

def save_run(filename, accuracy, transcription, cleaned_text):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO runs (filename, accuracy, transcription, cleaned_text)
        VALUES (?, ?, ?, ?)
    """, (filename, accuracy, transcription, cleaned_text))
    conn.commit()
    conn.close()

def get_all_runs():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM runs ORDER BY timestamp DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows