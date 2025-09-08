# Copyright (c) 2025, Haseeb Ali and contributors
# For license information, please see license.txt

# import frappe
import frappe
from frappe.model.document import Document


class RideBooking(Document):
	def validate(self):
		if not self.rate:
			self.rate=frappe.db.get_single_value("Rentals Settings", "standard_rate")
		total_distance = 0
			# Calculate total distance
		for item in self.items:
			total_distance += float(item.distance)
		self.total_amount = total_distance * self.rate