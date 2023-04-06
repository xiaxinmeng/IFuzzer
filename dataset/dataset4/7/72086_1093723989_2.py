with patch('xml.etree.ElementTree._escape_cdata', new=_escape_cdata):

    s = ET.tostring(root, encoding='unicode', method="xml")
print(s)