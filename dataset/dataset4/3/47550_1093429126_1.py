import cgi

fields = cgi.FieldStorage()
title = fields.getfirst('title')

print("Content-Type: text/html; charset=utf-8")
print("")

print('<p>Debug: %s</p>' % repr(title))
if title is None:
    print("No article selected")
else:
    print('<p>Information about %s.</p>' % cgi.escape(title))
#