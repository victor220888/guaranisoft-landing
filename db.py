import sqlite3
import os
from datetime import datetime
from pathlib import Path

# Path absoluto para que funcione sin importar el working directory
DB_DIR = Path(os.getenv("RENDER_DATA_DIR", str(Path(__file__).resolve().parent)))
DB_NAME = str(DB_DIR / "leads.db")

def init_db():
    try:
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
        print(f"[DB] Inicializada en: {DB_NAME}")
    except Exception as e:
        print(f"[DB ERROR] init_db: {e}")

def save_lead(nombre, empresa, telefono, email, mensaje):
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO leads (nombre, empresa, telefono, email, mensaje)
            VALUES (?, ?, ?, ?, ?)
        ''', (nombre, empresa, telefono, email, mensaje))
        conn.commit()
        conn.close()
        print(f"[DB] Lead guardado: {nombre} — {email}")
        return True
    except Exception as e:
        print(f"[DB ERROR] save_lead: {e}")
        return False

def get_all_leads():
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM leads ORDER BY fecha DESC')
        leads = cursor.fetchall()
        conn.close()
        return leads
    except Exception as e:
        print(f"[DB ERROR] get_all_leads: {e}")
        return []
