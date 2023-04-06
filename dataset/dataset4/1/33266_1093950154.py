import codecs

fout = codecs.open("test.utf-16", "wb", 'UTF-16')
fout.write(u"ABC")
fout.write(u"DEF")
fout.close()