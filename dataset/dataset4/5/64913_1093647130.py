if ']]>' in error_info:
    failureText = xml_document.createTextNode(error_info)
else:
    failureText = xml_document.createCDATASection(error_info)