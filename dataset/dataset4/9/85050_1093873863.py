import html
import xml.sax.saxutils as saxutils

print(saxutils.unescape("&reghard"))  # &reghard
print(html.unescape("&reghard"))  # ®hard