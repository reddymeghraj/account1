# Copyright (c) 2013, Wayzon and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Expence(Document):
	def on_submit(self):
		if self.payment_mode=='Cash':
			que=frappe.db.sql("""select max(cast(name as int)) from `tabCash`""")[0][0]
			if que:
				n=int(que)+1
			else:
				n=1	
			query=frappe.db.sql("""insert into `tabCash` set name=%s,amount=%s,date=%s,transaction='2',description=%s""",(n,self.amount,self.date,self.expence_type))
		else:
			query=frappe.db.sql("""select max(cast(name as int)) from `tabBalance`""")[0][0]
			if query:
				name=int(query)+1
			else:
				name=1
			q=frappe.db.sql("""insert into `tabBalance` set name=%s,bank=%s,bank_name=%s,amount=%s,transaction='2',date=%s,description=%s""",(name,self.bank,self.bank_name,self.amount,self.date,self.expence_type))	
			