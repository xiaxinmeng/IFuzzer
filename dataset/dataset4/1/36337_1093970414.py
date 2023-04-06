###
import xml.sax
import glob
from cStringIO import StringIO


class FooParser(xml.sax.ContentHandler):
    def __init__(self):
        self.bigcontent = StringIO()

    def startElement(self, name, attrs):
        pass

    def endElement(self, name):
        pass

    def characters(self, chars):
        self.bigcontent.write(chars)