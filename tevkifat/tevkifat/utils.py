def set_tevkifat_flag(doc, method=None):
    doc.custom_tevkifat_var_mi = 1 if doc.get("custom_tevkifat_kodu") else 0
