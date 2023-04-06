import codecs
f = open("syllables", "w+")
f2 = codecs.EncodedFile(f, "unicode_internal", "utf-8")
f2.write(u"a")
f2.close()