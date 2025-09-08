import frappe

def execute(filters=None):
	columns = [
		{
			"fieldname": "make",
			"label": "Make",
			"fieldtype": "Data",
			"width": 200
		},
		{
			"fieldname": "total_revenue",
			"label": "Total Revenue",
			"fieldtype": "Currency",
			"options": "PKR",
			"width": 150
		}
	]

	data = frappe.db.sql("""
		SELECT
			V.brand AS make,
			SUM(RB.total_amount) AS total_revenue
		FROM `tabRide Booking` RB
		JOIN `tabVehicle` V ON RB.vehicle = V.name
		WHERE RB.docstatus = 1
		GROUP BY V.brand
	""", as_dict=True)

	return columns, data
