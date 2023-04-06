from xml.sax import make_parser
from dtdcache.sax.saxutils import prepare_input_source # <- dtdcache
parser = make_parser()
inp = prepare_input_source('file:file.xhtml', cache="/tmp/xmlcache")