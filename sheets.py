"""
Integración Google Sheets — Leads Ñande ERP
Guarda cada lead del formulario en una hoja de Google Sheets compartida.
Requiere: service_account.json (no subir a git)
"""

import gspread
from datetime import datetime


def append_to_sheet(nombre, empresa, telefono, email, mensaje):
    """
    Agrega una fila al Google Sheet 'Leads Ñande ERP'.
    Retorna True si tuvo éxito, False si falló.
    """
    try:
        gc = gspread.service_account(filename='service_account.json')
        sh = gc.open("Leads Ñande ERP")
        worksheet = sh.sheet1

        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        worksheet.append_row([fecha, nombre, empresa, telefono, email, mensaje])
        return True
    except Exception as e:
        print(f"[GOOGLE SHEETS ERROR] {e}")
        return False
