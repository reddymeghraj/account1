# Copyright (c) 2013, Wayzon and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from datetime import datetime
class BalanceSheet(Document):
	pass
@frappe.whitelist()
def get_cash():
	qc=frappe.db.sql("""select sum(amount) from `tabCash` where transaction=1""")
	qc1=frappe.db.sql("""select sum(amount) from `tabCash` where transaction=2""")
	qb=frappe.db.sql("""select sum(amount) from `tabBalance` where transaction=1""")
	qb1=frappe.db.sql("""select sum(amount) from `tabBalance` where transaction=2""")
	bank_balance=qb[0][0]-qb1[0][0]
	cash=qc[0][0]-qc1[0][0]


	#BankWise
	qbw=frappe.db.sql("""select bank,bank_name,sum(amount) from `tabBalance` where transaction=1 group by bank""")
	length=len(qbw)
	options=[]
	for i in range(length):
		qbw1=frappe.db.sql("""select sum(amount) from `tabBalance` where transaction=2 and bank=%s""",qbw[i][0])
		amount=qbw[i][2]-qbw1[0][0]
		options.append(qbw[i][1])
		options.append(amount)
	length1=len(options)	
	d=datetime.now()
	d1=d.strftime('%Y-%m-%d')
	#Expence details
	qex=frappe.db.sql("""select expence_type,amount from `tabExpence` where date=%s""",d1)
	lgth=len(qex)
	html="""<html>
		
		<table>
		<tr>
		<td>
		<div class="well span2 cash alert-warning">
			<legend> <h4>Total Available Cash </h4></legend>
				<span class="icon-inr" style="width:"200">"""+str(cash)+"""</span>
		</div>
		</td>
		<td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
		<td>
		<div class="well span2 cash alert-warning">
			<legend> <h4> Total Bank Balance </h4></legend>
				<span class="icon-inr" style="width:"200">"""+str(bank_balance)+"""</span>
		</div>
		</td>
		</tr>
		</table>

		<table>
		<tr>
		<td width='550' style='text-align:center'><font color=red size=3>Bank Balance Sheet</font></td>
		<td width='50'></td>
		<td width='450' style='text-align:center'><font color=red size=3>Perticulers</font></td>
		</tr>
		<tr>
		<td>

		"""

	html1="""
		<table border='2'>
		<tr bgcolor="skyblue"><th width="150" style='text-align:center'>Sr. No.</th><th width='150' style='text-align:center'>Bank</th><th style='text-align:center' width='250'>Balance</td></tr>
		
		"""
	bal=''
	i=0
	k=0
	while i < length1-1:
		x=options[i]
		y=options[i+1]
		i=i+2
		k=k+1
		z="""
			<tr bgcolor='lightblue'>
			<td style='text-align:center'>%s</td>
			<td style='text-align:center'>%s</td>
			<td style='text-align:center'>%s</td>
			
			</tr>"""%(k,x,y)
		bal=bal+z	
	x="""</table>
	</td>
	<td>
		
	</td>
	<td>"""
	html2="""
			 <table border=2>
			 	<tr bgcolor="skyblue"><th width='150' style='text-align:center'>Perticular</th><th style='text-align:center' width='250'>Amount</td></tr>
				
		"""
	blank=''
	l=0	
	while l < lgth:
		n=qex[l][0]
		m=qex[l][1]
		l=l+1
		c="""
			<tr bgcolor='lightblue'>
			<td style='text-align:center'>%s</td>
			<td style='text-align:center'>%s</td>
			</tr>"""%(n,m)
		blank=blank+c	
	h="""</td>
	</tr>
	</table>
	</html>"""
	v=html1+bal+x+html2+blank+h
	return html+v

