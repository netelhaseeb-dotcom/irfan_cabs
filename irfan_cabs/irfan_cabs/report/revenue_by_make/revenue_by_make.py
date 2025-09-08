import frappe


def execute(filters=None):
	columns = [
		{
			"fieldname": "make",
			"label": "Make",
			"fieldtype": "Data"
		},
		{
			"fieldname": "total_revenue",
			"label": "Total Revenue",
			"fieldtype": "Currency",
			"options": "PKR"
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

	chart = {
		"type": "bar",
		"data": {
			"labels": [d.make for d in data],
			"datasets": [{
				"label": "Total Revenue",
				"data": [d.total_revenue for d in data],
				"backgroundColor": "rgba(75, 192, 192, 0.2)",
				"borderColor": "rgba(75, 192, 192, 1)",
				"borderWidth": 1
			}]
		},
		"options": {
			"scales": {
				"x": {
					"beginAtZero": True
				}
			}
		}
	}

	return columns, data , "Here is the revenue by make report", None, chart