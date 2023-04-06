import xml.sax
import xml.sax.handler
import xml.sax.saxutils
x = '''<?xml version="1.0"?><mechanisms xmlns='urn:ietf:
params:xml:ns:xmpp-sasl'
>'''
parser = xml.sax.make_parser()
parser.setFeature(xml.sax.handler.feature_namespaces, True)
parser.setContentHandler(xml.sax.saxutils.XMLGenerator())
parser.feed(x)