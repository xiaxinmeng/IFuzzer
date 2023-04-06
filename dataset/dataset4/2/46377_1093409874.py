parser = xml.sax.make_parser()
parser.setEntityResolver(CachingEntityResolver())
doc = xml.dom.minidom.parse('file.xml', parser)