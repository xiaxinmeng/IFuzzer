import xml.etree.ElementTree
import sys

e = xml.etree.ElementTree.parse(sys.argv[1]).getroot()
for outline in e.iter('outline'):
	if "type" in outline.attrib and outline.attrib["type"] == "rss":
		url = outline.attrib['xmlUrl']
		name = outline.attrib['title']#.encode("utf-8")
		print("%s youtube \"~%s\"" % (url, str(name)))