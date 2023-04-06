import xml.sax
import StringIO

# Some StringIO buffer.
source = StringIO.StringIO(b'<_/>')

# Do some parsing.
xml.sax.parse(source, xml.sax.handler.ContentHandler())

# Try to do some other parsing (fails).
xml.sax.parse(source, xml.sax.handler.ContentHandler())