import sqlite3

# Connect to SQLite database (creates the file if it doesn't exist)
conn = sqlite3.connect('self_care_journal.db')
c = conn.cursor()

# Create tables for moods and journals
c.execute('''
CREATE TABLE IF NOT EXISTS moods (
    id INTEGER PRIMARY KEY,
    mood TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')
c.execute('''
CREATE TABLE IF NOT EXISTS journals (
    id INTEGER PRIMARY KEY,
    entry TEXT,
    mood TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')
conn.commit()
conn.close()
