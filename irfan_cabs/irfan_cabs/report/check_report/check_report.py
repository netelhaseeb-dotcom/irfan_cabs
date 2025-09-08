import frappe

def execute(filters=None):
    columns = [
        {
            "fieldname": "make",
            "label": "Make",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "fieldname": "total_revenue",
            "label": "Total Revenue",
            "fieldtype": "Currency",
            "width": 150
        }
    ]

    data = frappe.db.sql("""
        SELECT
            V.make AS make,
            SUM(RB.total_amount) AS total_revenue
        FROM `tabRide Booking` RB
        JOIN `tabVehicle` V ON RB.vehicle = V.name
        WHERE RB.docstatus = 1
        GROUP BY V.make
    """, as_list=True)  # use as_list=True if returning list of lists

    return columns, data
