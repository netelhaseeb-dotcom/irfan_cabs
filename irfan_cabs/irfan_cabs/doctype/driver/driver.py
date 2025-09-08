# Copyright (c) 2025, Haseeb Ali and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Driver(Document):
	def before_save(self):
		full_name=f"{self.first_name} {self.last_name}"
		self.full_name=full_name

