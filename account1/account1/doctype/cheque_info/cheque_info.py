# Copyright (c) 2013, Wayzon and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class ChequeInfo(Document):
	def on_submit(self):
		query=frappe.db.sql("""select max(cast(name as int)) from `tabBalance`""")[0][0]
		if query:
			name=int(query)+1
		else:
			name=1
		q=frappe.db.sql("""insert into `tabBalance` set name=%s,bank=%s,bank_name=%s,party=%s,party_name=%s,client_name=%s,contact_no=%s,cheque_no=%s,amount=%s,transaction=%s,date=%s,description=%s""",(name,self.bank,self.bank_name,self.party,self.party_name,self.client_name,self.contact_no,self.cheque_no,self.amount,self.transaction,self.date,self.description))	
		q1=frappe.db.sql("""update `tabCheque Info` set status='cleared' where bank=%s and cheque_no=%s and date=%s and status=%s""",(self.bank,self.cheque_no,self.date,self.status))	
