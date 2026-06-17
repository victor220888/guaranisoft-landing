import sqlite3
from datetime import datetime

DB_NAME = "leads.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            empresa TEXT,
            telefono TEXT,
            email TEXT NOT NULL,
            mensaje TEXT NOT NULL,
            fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def save_lead(nombre, empresa, telefono, email, mensaje):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO leads (nombre, empresa, telefono, email, mensaje)
        VALUES (?, ?, ?, ?, ?)
    ''', (nombre, empresa, telefono, email, mensaje))
    conn.commit()
    conn.close()

def get_all_leads():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM leads ORDER BY fecha DESC')
    leads = cursor.fetchall()
    conn.close()
    return leads