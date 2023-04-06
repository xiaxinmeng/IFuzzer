from io import StringIO
txt = StringIO('0123456789')
txt.seek(15,0) # no problem with absolute seek
txt.write('xxx')
s  = txt.getvalue()
print(ord(s[12]))
# 0