from xml.sax import make_parser
from xml.sax.saxutils import prepare_input_source
parser = make_parser()
inp = prepare_input_source('file:file.xhtml')
parser.parse(inp)