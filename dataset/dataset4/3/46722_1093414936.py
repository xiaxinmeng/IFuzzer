import dl
libc = dl.open("libc.so.6")
iconv = libc.call("iconv_open", "ISO-8859-1", "ISO-8859-2")
print(iconv)