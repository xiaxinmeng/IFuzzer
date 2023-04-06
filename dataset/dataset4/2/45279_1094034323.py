from io import BytesIO
from xml.etree.ElementTree import ElementTree
content = "<?xml version='1.0' encoding='UTF-16'?><html></html>"
input = BytesIO(content.encode('utf-16'))
tree = ElementTree()
tree.parse(input)
# Write content
output = BytesIO()
tree.write(output, encoding="utf-16")
assert output.getvalue().decode('utf-16') == content