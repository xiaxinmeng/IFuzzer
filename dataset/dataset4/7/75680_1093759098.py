import xml.etree.ElementTree as etree

def test():
    parser = etree.XMLParser()
    try:
        parser.close()
    except etree.ParseError as exc:
        e = exc  # must keep local reference!

test()