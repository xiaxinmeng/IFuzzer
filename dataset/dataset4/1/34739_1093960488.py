f = open(file)
codestring = f.read()
codestring = codestring.replace("\r\n","\n")
codestring = codestring.replace("\r","\n")