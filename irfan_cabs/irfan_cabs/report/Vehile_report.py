# vehicle_report.py
import frappe

def execute(filters=None):
    columns = [
        {"label": "Vehicle Name", "fieldname": "name", "fieldtype": "Link", "options": "Vehicle", "width": 150},
        {"label": "Brand", "fieldname": "brand", "fieldtype": "Data", "width": 100},
        {"label": "Model", "fieldname": "model", "fieldtype": "Data", "width": 100},
        {"label": "Status", "fieldname": "status", "fieldtype": "Data", "width": 100},
    ]

    data = frappe.db.get_all("Vehicle",
        fields=["name", "brand", "model", "status"],
        order_by="modified desc"
    )

    return columns, data
