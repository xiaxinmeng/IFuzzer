from xml.etree import ElementTree as ET
for result in ET.iterparse('example.xml', events=('start', 'end')):
    print(result)