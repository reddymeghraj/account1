# Copyright (c) 2013, Wayzon and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class BankDeposit(Document):
	def on_submit(self):
		que=frappe.db.sql("""select max(cast(name as int)) from `tabCash`""")[0][0]
		if que:
			n=int(que)+1
		else:
			n=1	
		query=frappe.db.sql("""insert into `tabCash` set name=%s,amount=%s,date=%s,transaction='2',description='Deposited in Bank'""",(n,self.amount,self.date))
		query=frappe.db.sql("""select max(cast(name as int)) from `tabBalance`""")[0][0]
		if query:
			name=int(query)+1
		else:
			name=1
		q=frappe.db.sql("""insert into `tabBalance` set name=%s,bank=%s,bank_name=%s,amount=%s,transaction='1',date=%s,description='Deposited Amount'""",(name,self.bank,self.bank_name,self.amount,self.date))	