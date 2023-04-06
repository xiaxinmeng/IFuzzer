import sys
print(sys.version) # for help verifying version tested
from xml.etree import ElementTree

sampleinput = """<?xml version="1.0"?><Hello></Hello>"""
xmlobj = ElementTree.fromstring(sampleinput)
type(xmlobj)
xmlstr = ElementTree.tostring(xmlobj,'utf-8')
print("xmlstr value is '", xmlstr, "'", sep="")
print("xmlstr type is '", type(xmlstr), "'", sep="")