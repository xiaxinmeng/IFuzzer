import io

from xml.etree.ElementTree import parse

stream = io.StringIO()

stream.write('''<?xml version="1.0"?>
<site>
</site>
''')

stream.seek(0)

parsed = parse(stream)

print(parsed)