tree = ET.ElementTree()
stream = io.BytesIO()
stream.write(b'''<?xml version="1.0"?>
<site>
</site>
''')
stream.seek(0)
tree.parse(stream)

print(tree.getroot())