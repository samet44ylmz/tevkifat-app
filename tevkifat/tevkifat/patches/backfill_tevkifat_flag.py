import frappe

def execute():
    frappe.db.sql("""
        UPDATE `tabSales Invoice`
        SET custom_tevkifat_var_mi = IF(IFNULL(custom_tevkifat_kodu,'')='', 0, 1)
    """)
