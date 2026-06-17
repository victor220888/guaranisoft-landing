"""
Integración Google Sheets — Leads GuaraníSoft
Guarda cada lead del formulario en una hoja de Google Sheets compartida.
Requiere: service_account.json (no subir a git)

Sheet: "Leads GuaraníSoft"
  - Pestaña "Ñande ERP"  → leads del producto ERP
  - Pestaña "Ñande CRM"  → leads del producto CRM (futuro)
"""

import gspread
from datetime import datetime

SHEET_NAME = "Leads GuaraníSoft"
WORKSHEET_ERP = "Ñande ERP"
WORKSHEET_CRM = "Ñande CRM"


def _get_worksheet(name):
    """Conecta al Sheet y devuelve la worksheet especificada."""
    gc = gspread.service_account(filename='service_account.json')
    sh = gc.open(SHEET_NAME)
    try:
        return sh.worksheet(name)
    except Exception:
        # Si la pestaña no existe, la crea con encabezados
        ws = sh.add_worksheet(title=name, rows=1000, cols=10)
        ws.append_row(["Fecha", "Nombre", "Empresa", "Teléfono", "Email", "Mensaje"])
        return ws


def append_to_sheet(nombre, empresa, telefono, email, mensaje, producto="erp"):
    """
    Agrega una fila al Google Sheet.
    producto: "erp" → pestaña Ñande ERP, "crm" → pestaña Ñande CRM
    Retorna True si tuvo éxito, False si falló.
    """
    try:
        if producto == "crm":
            ws = _get_worksheet(WORKSHEET_CRM)
        else:
            ws = _get_worksheet(WORKSHEET_ERP)

        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ws.append_row([fecha, nombre, empresa, telefono, email, mensaje])
        return True
    except Exception as e:
        print(f"[GOOGLE SHEETS ERROR] {e}")
        return False
