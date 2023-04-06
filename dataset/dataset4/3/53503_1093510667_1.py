from xml.etree import cElementTree as cET
for result in cET.iterparse('example.xml', events=(b'start', b'end')):
    print(result)