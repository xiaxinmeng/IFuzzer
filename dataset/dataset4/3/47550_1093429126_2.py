import sys
import cgi

def printu8(*args):
    """Prints to stdout encoding as utf-8, rather than the current terminal
    encoding. (Not a fully-featured print function)."""
    sys.stdout.write(' '.join([x.encode('utf-8') for x in args]))
    sys.stdout.write('\n')

fields = cgi.FieldStorage()
title = fields.getfirst('title')
if title is not None:
    title = str(title).decode("utf-8", "replace")

print("Content-Type: text/html; charset=utf-8")
print("")

print('<p>Debug: %s.</p>' % repr(title))
if title is None:
    print("No article selected.")
else:
    printu8('<p>Information about %s.</p>' % cgi.escape(title))
#