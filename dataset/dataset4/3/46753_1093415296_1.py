# sax.py
import sys
import xml.sax
BUG = True
class SaxHandler(xml.sax.handler.ContentHandler):
    def startElement(self, name, attributes):
        print("+", name)
    def endElement(self, name):
        print("-", name)
handler = SaxHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
if BUG:
    parser.parse(sys.argv[1])
else:
    fh = open(sys.argv[1], encoding="utf8")
    parser.parse(fh)
    fh.close()
print("Done")
# end of sax.py