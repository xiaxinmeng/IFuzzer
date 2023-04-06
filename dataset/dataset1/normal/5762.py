#!/usr/bin/python
from xml.dom import minidom

samplexml = """
<element xmlns=""/>
"""

if __name__ == '__main__':
  doc = minidom.parseString(samplexml)
  doc.toxml()
