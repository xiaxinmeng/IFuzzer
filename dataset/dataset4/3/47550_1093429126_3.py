import sys
import cgi

def printu8(*args):
    """Prints to stdout encoding as utf-8, rather than the current terminal
    encoding. (Not a fully-featured print function)."""
    sys.stdout.buffer.write(b' '.join([x.encode('utf-8') for x in args]))
    sys.stdout.buffer.write(b'\n')

fields = cgi.FieldStorage()
title = fields.getfirst('title')
# Note: No call to decode. I have no opportunity to specify the encoding
since
# it comes straight out of FieldStorage as a Unicode string.

print("Content-Type: text/html; charset=utf-8")
print("")

print('<p>Debug: %s.</p>' % ascii(title))
if title is None:
    print("No article selected.")
else:
    printu8('<p>Information about %s.</p>' % cgi.escape(title))
#